const carousel = document.querySelector('.carousel');
const cards = document.querySelectorAll('.card');
const prevButton = document.querySelector('.nav-btn.left');
const nextButton = document.querySelector('.nav-btn.right');

let activeIndex = 0;

const updateCarousel = () => {
    cards.forEach((card, index) => {
        card.classList.remove('active', 'next', 'prev');
        if (index === activeIndex) {
            card.classList.add('active');
        } else if (index === (activeIndex + 1) % cards.length) {
            card.classList.add('next');
        } else if (index === (activeIndex - 1 + cards.length) % cards.length) {
            card.classList.add('prev');
        }
    });
};

nextButton.addEventListener('click', () => {
    activeIndex = (activeIndex + 1) % cards.length;
    updateCarousel();
});

prevButton.addEventListener('click', () => {
    activeIndex = (activeIndex - 1 + cards.length) % cards.length;
    updateCarousel();
});

updateCarousel();