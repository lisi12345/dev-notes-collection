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