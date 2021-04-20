import "./App.css";
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { useEffect } from "react";
import Nav from "./Components/Nav"
import Projects from "./Components/Projects"
import Blogs from "./Components/Blogs"
import Works from "./Components/Works"
import Home from "./Components/Home"
import Footer from "./Components/Footer"
import Open from "./Components/Opening"

function App(props) {
  return (
    <>
      <Router>
        <Switch>
          <Route exact path="/">
            <Nav />
            <Open />
            <Home />
            <Footer />
          </Route>

          <Route exact path="/project">
            <Nav />
            <Projects />
          </Route>

          <Route exact path="/work">
            <Nav />
            <Works />
          </Route>

          <Route exact path="/blog">
            <Nav />
            <Blogs />
          </Route>
        </Switch>
      </Router>
    </>
  )
}

export default App
