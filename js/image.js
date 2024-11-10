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
        this.src = "images/default_image.jpg";
        this.alt = "default image";
        // <!--
        // onerror="this.onerror=null; this.src='../images/default_image.jpg';"
        // -->
        // this.style.display = "none"
    }
    
  });