const clockElement = document.getElementById("clockFace");

function twoDigit(n) {
  if (n < 10) {
    return "0" + n;
  } else {
    return "" + n;
  }
}

const stringLen = "00:00:00 AM".length * 2;
const hslDelta = 360 / stringLen;
let hslStart = 0;

function runIt() {
  const date = new Date();
  const h = date.getHours();
  const hours = twoDigit(h <= 12 ? h : h - 12);
  const minutes = twoDigit(date.getMinutes());
  const seconds = twoDigit(date.getSeconds());
  const ampm = h < 12 ? "AM" : "PM";
  const fullString = `${hours}:${minutes}:${seconds} ${ampm}`;
  let hslVal = hslStart;
  hslStart = (hslStart + 1) % 360;
  /*
  let rainbowString = ''
  for (let c of fullString) {
    rainbowString += `<span style="color: hsl(${hslVal}, 80%, 50%)">${c}</span>`;
    hslVal += hslDelta;
    if (hslVal >= 360) { hslVal = 0; }
  }
  clockElement.innerHTML = rainbowString;
  */
  requestAnimationFrame(runIt);
  clockElement.innerHTML = `${hours}:${minutes}:${seconds} ${ampm}`;
}

requestAnimationFrame(runIt);

async function startIt() {
  const statusElem = document.getElementById("status");
  if ("wakeLock" in navigator) {
    isSupported = true;
    statusElem.textContent = "Screen Wake Lock API supported!";
    // Create a reference for the Wake Lock.
    let wakeLock = null;

    // create an async function to request a wake lock
    try {
      wakeLock = await navigator.wakeLock.request("screen");
      statusElem.textContent = "Wake Lock is active!";
    } catch (err) {
      // The Wake Lock request has failed - usually system related, such as battery.
      statusElem.textContent = `${err.name}, ${err.message}`;
    }
  } else {
    wakeButton.disabled = true;
    statusElem.textContent = "Wake lock is not supported by this browser.";
  }
}
startIt();
