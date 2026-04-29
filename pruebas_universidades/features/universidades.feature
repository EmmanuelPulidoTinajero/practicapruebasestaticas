Feature: Busqueda en portales universitarios
  Como estudiante
  Quiero buscar informacion en los sitios universitarios desde Google
  Para validar que el flujo de busqueda funciona con BDD, DDT y Selenium

  Scenario: Buscar ITESO en Google y consultar carreras
    Given que abro Google
    When busco en Google "iteso" y entro al primer resultado de "iteso.mx"
    Then valido que estoy en la pagina de "iteso.mx"
    When busco internamente "carreras"
    Then valido que se muestran resultados relacionados con "carreras"

  Scenario Outline: Buscar universidades en Google y consultar terminos internos
    Given que abro Google
    When busco en Google "<termino_google>" y entro al primer resultado de "<dominio>"
    Then valido que estoy en la pagina de "<dominio>"
    When busco internamente "<termino_interno>"
    Then valido que se muestran resultados relacionados con "<termino_interno>"

    Examples:
      | termino_google    | dominio  | termino_interno |
      | iteso             | iteso.mx | becas           |
      | universidad udg   | udg.mx   | licenciaturas   |
      | tec de monterrey  | tec.mx   | ingenieria      |