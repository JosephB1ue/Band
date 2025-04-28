function toggleActiveClass(element) {
    if (element.classList.contains("active"))
      element.classList.remove("active");
    else element.classList.add("active");
  }

  let toggleBtn = document.querySelectorAll(".wish");
  for (let i = 0; i < toggleBtn.length; i++) {
    toggleBtn[i].addEventListener("click", () =>
      toggleActiveClass(toggleBtn[i])
    );
  }