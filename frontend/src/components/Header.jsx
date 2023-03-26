import React, { useEffect } from 'react';


const handleClickAside = (e) => {
	const dropdownIcon = e.currentTarget.getElementsByClassName('icon')[0].getElementsByClassName('mdi')[0];
	document.documentElement.classList.toggle('aside-mobile-expanded');
	dropdownIcon.classList.toggle('mdi-forwardburger');
	dropdownIcon.classList.toggle('mdi-backburger');
}

const handleClickNavbar = (e) => {
	const dropdownIcon = e.currentTarget.getElementsByClassName('icon')[0].getElementsByClassName('mdi')[0];
	document.getElementById(e.currentTarget.getAttribute('data-target')).classList.toggle('active');
	dropdownIcon.classList.toggle('mdi-dots-vertical');
	dropdownIcon.classList.toggle('mdi-close');
}


const Header = () => {

    useEffect(() => {
		Array.from(document.getElementsByClassName('mobile-aside-button')).forEach((el) => {
			el.addEventListener('click', handleClickAside);
		});

		Array.from(document.getElementsByClassName('--jb-navbar-menu-toggle')).forEach((el) => {
			el.addEventListener('click', handleClickNavbar);
		});
	}, []);

    return (
        <nav id="navbar-main" className="navbar is-fixed-top">
            <div className="navbar-brand">
                <button type='button' className="navbar-item mobile-aside-button">
                    <span className="icon"><i className="mdi mdi-forwardburger mdi-24px"></i></span>
                </button>
            </div>
            <div className="navbar-brand is-right">
                <button type='button' className="navbar-item --jb-navbar-menu-toggle" data-target="navbar-menu">
                    <span className="icon"><i className="mdi mdi-dots-vertical mdi-24px"></i></span>
                </button>
            </div>
            <div className="navbar-menu" id="navbar-menu">
                <div className="navbar-end">
                    <a href="http://hoangvangioi.com/" className="navbar-item has-divider desktop-icon-only">
                        <span className="icon"><i className="mdi mdi-help-circle-outline mdi-24px"></i></span>
                        <span>About</span>
                    </a>
                    <a href="https://github.com/hoangvangioi" className="navbar-item has-divider desktop-icon-only">
                        <span className="icon"><i className="mdi mdi-github mdi-24px"></i></span>
                        <span>GitHub</span>
                    </a>
                </div>
            </div>
        </nav>
    );
};

export default Header;