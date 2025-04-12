window.addEventListener("scroll", function() {
    const header = document.getElementById("main-header");
    if (window.scrollY > 1) {
      header.classList.add("sticky");
    } else {
      header.classList.remove("sticky");
    }
  });

  