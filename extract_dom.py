import asyncio
import os
# pyrefly: ignore [missing-import]
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('http://localhost:8501')
        
        # Wait for page elements to load
        await page.wait_for_timeout(3000)
        
        # Get body outerHTML
        html = await page.content()
        
        output_path = r'd:\Joki\SafeSpace\dom_debug.html'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Successfully saved DOM to {output_path}")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
