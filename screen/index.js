const puppeteer = require('puppeteer');
(async () => {
        const browser = await puppeteer.launch({executablePath: '/usr/bin/chromium-browser'});
        const page = await browser.newPage();
        await page.goto('http://localhost');
	await page.setViewport({ width: 800, height: 480});
	await page.waitFor(1000)
        await page.screenshot({path: 'eink.png'});
        await browser.close();
})();
