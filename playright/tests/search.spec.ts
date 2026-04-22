import { test, expect } from '@playwright/test';

const queries = ['Hello, world!', 'Iteso', 'Amazon'];

test.describe('Google Search', () => {
  for (const query of queries) {
    test(`Searching for "${query}" on Google`, async ({ page }) => {
      await page.goto('https://www.google.com');
      const searchBox = page.locator('#APjFqb');
      await searchBox.fill(query);
      await searchBox.press('Enter');
      await page.waitForSelector('#rcnt');
      const title = await page.title();
      expect(title.startsWith(query)).toBe(true);
    });
  }
});
