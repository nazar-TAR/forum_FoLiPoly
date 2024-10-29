const button = document.getElementById("nav-burger")
    const burger_page = document.getElementById("nav-burger-page")
  function toggleMenu(){
        document.body.classList.toggle("lock-scroll");
    button.classList.toggle('is-active');
        burger_page.classList.toggle('burger-page__is-active')

  };
