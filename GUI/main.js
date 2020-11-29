const { app, BrowserWindow } = require("electron");
const path = require("path");
const url = require("url");
let win;
function createWindow() {
  let config = {
    width: 800,
    height: 600,
    autoHideMenuBar: false,
    frame: true,
    backgroundColor: "rgb(19,17,15)",
    show: true,
    icon: path.join(__dirname, "./img/ai.ico"),
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
