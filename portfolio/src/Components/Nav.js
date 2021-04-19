import React, {useState} from 'react'

function Nav() {
    const [active, setActive] = useState(false)
    const handleClick = e =>{
        setActive(!active)
    }

    return (
        <>
        <nav>
            <div className="hamburger" onClick={handleClick}>
                <div className="line"></div>
                <div className="line"></div>
                <div className="line"></div>
            </div>
            <a className="brand" href="/">HOME</a>
            <ul className={active ? "nav-links open" : "nav-links"}>
                <li className={active ? "nav-link fade" : "nav-link"}><a href="project">PROJECT</a></li>
                <li className={active ? "nav-link fade" : "nav-link"}><a href="work">WORK</a></li>
                <li className={active ? "nav-link fade" : "nav-link"}><a href="blog">BLOG</a></li>
            </ul>
        </nav>  
        </>
    )
}

export default Nav
