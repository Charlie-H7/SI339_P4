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

//   function setTheme(theme) {
//     // Remove any previous theme classes
//     document.body.classList.remove('light-mode', 'dark-mode', 'system-dark', 'high-contrast');

//     if (theme === 'dark') {
//         document.body.classList.add('dark-mode');
//         localStorage.setItem('theme', 'dark');
//     } else if (theme === 'light') {
//         document.body.classList.add('light-mode');
//         localStorage.setItem('theme', 'light');
//     } else if (theme === 'high-contrast') {
//         document.body.classList.add('high-contrast');
//         localStorage.setItem('theme', 'high-contrast');
//     } else {
//         // Use system preference for "System Default"
//         if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
//             document.body.classList.add('dark-mode');
//         }
       
//         localStorage.setItem('theme', 'system');
//     }
// }

// // Load saved theme from localStorage or fallback to system preference
// function loadTheme() {
//     const savedTheme = localStorage.getItem('theme') || 'system';
//     document.getElementById('theme-select').value = savedTheme;
//     setTheme(savedTheme);
// }

// loadTheme();



// theme
document.getElementById("theme-switch").addEventListener("change", function () {
    console.log("Color scheme preference has been changed to ", this.value);
    document.body.className = this.value;
});

// COLOR SCHEME DETECTOR
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