from urllib.parse import parse_qs, quote_plus, urlparse

from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


CONFIG_DOMINIOS = {
    "iteso.mx": {
        "selectors": [
            (By.NAME, "s"),
            (By.CSS_SELECTOR, "input[type='search']"),
            (By.CSS_SELECTOR, "input[placeholder*='Buscar']"),
        ],
        "search_url_template": "https://iteso.mx/?s={query}",
    },
    "udg.mx": {
        "selectors": [
            (By.ID, "edit-keys"),
            (By.NAME, "keys"),
            (By.CSS_SELECTOR, "input[type='search']"),
        ],
        "search_url_template": "https://www.udg.mx/es/busqueda?keys={query}",
    },
    "tec.mx": {
        "selectors": [
            (By.CSS_SELECTOR, "input[type='search']"),
            (By.NAME, "q"),
            (By.CSS_SELECTOR, "input[placeholder*='Buscar']"),
        ],
        "search_url_template": "https://tec.mx/es/search?keys={query}",
    },
}


def _dominio_actual(url: str) -> str | None:
    for dominio in CONFIG_DOMINIOS:
        if dominio in url:
            return dominio
    return None


def _buscar_input_clickable(driver, selectors, timeout=8):
    wait = WebDriverWait(driver, timeout)
    for selector in selectors:
        try:
            element = wait.until(EC.element_to_be_clickable(selector))
            return element
        except Exception:
            continue
    return None


def _aceptar_consentimiento_google(driver):
    botones = [
        (By.XPATH, "//button[.//div[contains(., 'Aceptar todo')]]"),
        (By.XPATH, "//button[contains(., 'Aceptar todo')]"),
        (By.XPATH, "//button[contains(., 'Accept all')]"),
        (By.XPATH, "//div[@role='button' and contains(., 'Aceptar todo')]"),
    ]
    for selector in botones:
        try:
            boton = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(selector))
            boton.click()
            return
        except Exception:
            continue


def _href_contiene_dominio(href: str, dominio: str) -> bool:
    if not href:
        return False
    href = href.strip()
    if dominio in href:
        return True

    parsed = urlparse(href)
    if "google." in (parsed.netloc or "") and parsed.path.startswith("/url"):
        destino = parse_qs(parsed.query).get("q", [""])[0]
        return dominio in destino

    return False


@given("que abro Google")
def step_abrir_google(context):
    context.driver.get("https://www.google.com/ncr")
    context.driver.maximize_window()
    _aceptar_consentimiento_google(context.driver)


@when('busco en Google "{termino}" y entro al primer resultado de "{dominio}"')
def step_google_y_abrir_resultado(context, termino, dominio):
    wait = WebDriverWait(context.driver, 20)
    context.driver.get(f"https://www.google.com/search?q={quote_plus(termino)}&hl=es")
    _aceptar_consentimiento_google(context.driver)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href]")))
    enlaces = context.driver.find_elements(By.CSS_SELECTOR, "a[href]")

    for enlace in enlaces:
        href = enlace.get_attribute("href")
        if _href_contiene_dominio(href, dominio):
            context.driver.execute_script("arguments[0].click();", enlace)
            break
    else:
        context.driver.get(f"https://{dominio}")

    wait.until(EC.url_contains(dominio))
    context.dominio_actual = dominio


@then('valido que estoy en la pagina de "{dominio}"')
def step_validar_dominio(context, dominio):
    WebDriverWait(context.driver, 15).until(EC.url_contains(dominio))


@when('busco internamente "{termino}"')
def step_busqueda_interna(context, termino):
    url_actual = context.driver.current_url
    dominio = getattr(context, "dominio_actual", None) or _dominio_actual(url_actual)
    if dominio is None:
        raise AssertionError(f"No se pudo identificar el dominio con la URL actual: {url_actual}")

    config = CONFIG_DOMINIOS[dominio]
    input_busqueda = _buscar_input_clickable(context.driver, config["selectors"])

    if input_busqueda:
        input_busqueda.clear()
        input_busqueda.send_keys(termino)
        input_busqueda.send_keys(Keys.RETURN)
    else:
        query = quote_plus(termino)
        context.driver.get(config["search_url_template"].format(query=query))

    context.termino_actual = termino


@then('valido que se muestran resultados relacionados con "{termino}"')
def step_validar_resultados(context, termino):
    wait = WebDriverWait(context.driver, 15)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    pagina = context.driver.page_source.lower()
    termino_normalizado = termino.strip().lower()
    raiz = termino_normalizado[:-1] if termino_normalizado.endswith("s") else termino_normalizado

    if termino_normalizado not in pagina and raiz not in pagina:
        raise AssertionError(
            f"No se encontraron coincidencias para '{termino}' en la pagina de resultados. "
            f"URL actual: {context.driver.current_url}"
        )