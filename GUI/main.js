const { app, BrowserWindow } = require("electron");
const path = require("path");
const url = require("url");
let win;
function createWindow() {
  let config = {
    width: 900,
    height: 700,
    autoHideMenuBar: true,
    icon: path.join(__dirname, "./img/ai2.ico"),
    webPreferences: {
      nodeIntegration: true,
    },
  };
  win = new BrowserWindow(config);
  win.loadURL(
    url.format({
      pathname: path.join(__dirname, "index.html"),
      protocol: "file:",
      slashes: true,
    })
  );

  win.once("ready-to-show", () => {
    win.show();
  });
  win.on("closed", () => {
    win = null;
  });
}
app.on("ready", createWindow);
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
app.on("activate", () => {
  if (win === null) {
    createWindow();
  }
});
