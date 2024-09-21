document.addEventListener('DOMContentLoaded', (event) => {
    // Mobilbarát menü toggle
    const menuItems = document.querySelectorAll('.menu > li');
    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            if (window.innerWidth <= 600) {
                const submenu = this.querySelector('.submenu');
                if (submenu) {
                    e.preventDefault();
                    submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
                }
            }
        });
    });
});