Use the site: https://react.dev/
---
## Download Node.js
- https://nodejs.org/en/download
- OR use nvm
  
## Update Node.js and npm
1. Download nvm
   1. Windows: https://github.com/coreybutler/nvm-windows
   2. Download nvm-setup.exe
   3. Run the installer
   4. Restart your PowerShell or terminal if you have already opened
   5. Check if installed successfully: nvm -v
2. Update Node.js
   1. Browse Node.js versions: nvm ls available
   2. Select a version to download: nvm install <version>
      1. For example: nvm install 21.6.2
   3. nvm use <version>
      1. For example: nvm use 21.6.2
   4.  Check node.js version: node -v
3. Update npm: npm install npm@latest -g

---
# Create a Next.js project
https://nextjs.org/learn/dashboard-app/getting-started

- npx create-next-app@latest <folder name> --use-npm  
    - For example: npx create-next-app@latest src --use-npm  
- npm run dev

---
## Dark Mode
- [NextUI](https://nextui.org/docs/customization/dark-mode)
   1. Hard coded: Add ***className="dark text-foreground bg-background"*** to **<NextUIProvider>** or other HTML tag.
   2. Dynamic switching mode/theme: use [next-themes](https://github.com/pacocoursey/next-themes)
- [tailwind css](https://tailwindcss.com/docs/dark-mode)

---
## Issues and solutions
#### Issue: 
The web app fails to load data at the first launch, but the problem goes away after refreshing the page.
#### Description
When first click localhost link, the console prompts "*Uncaught SyntaxError: Invalid or unexpected token (at layout.js:356:29)*", and the page does not query data nor have any data shown. After a certain of time period, an error "*ChunkLoadError: Loading chunk app/layout failed.
(timeout: http://localhost:3000/_next/static/chunks/app/layout.js)*" prompts.
![alt text](image.png)

Until now (5/23/2024), I have not deploy the app, so I'm not sure if the same issue will still exist in production.
#### Solution:
1. Stop the app
2. Delete .next folder
3. Clear browser cache and hard refresh by Fn + F5
4. Re-run the app

