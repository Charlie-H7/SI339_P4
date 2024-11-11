function toggleNav() {
    const sidebar = document.getElementById("sidebar");
    if (sidebar.style.width === "250px") {
      sidebar.style.width = "0";
    } else {
      sidebar.style.width = "250px";
    }
  }

  document.querySelectorAll('img').forEach(img => {
    console.log("fetching image")
    img.onerror = function () {
        this.onerror = null;
        this.src = "../images/default_image.jpg";
        this.alt = "default image";
        // <!--
        // onerror="this.onerror=null; this.src='../images/default_image.jpg';"
        // -->
        // this.style.display = "none"
    }
    
  });





// theme
document.getElementById("theme-switch").addEventListener("change", function () {
    console.log("Theme changed: ", this.value);
    document.body.className = this.value; //Picks the corresponding theme
});

// Color Scheme
function setColorScheme() {
    lightMode = window.matchMedia('(prefers-color-scheme: light)').matches;
    darkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
    highContrast = window.matchMedia('(prefers-contrast: high)').matches;

    if (lightMode) {
        document.body.className = 'light-mode';
        console.log("light");
    } 
    else if (darkMode) {
        document.body.className = 'dark-mode';
        console.log("dark");
    } 
    else if (highContrast) {
        document.body.className = 'high-contrast';
        console.log("cont");
    } 
    else {
        document.body.className = 'dark-mode';
        // def

    }
};

setColorScheme();