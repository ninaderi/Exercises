import React from 'react';
import './Header.css';
import ReactImg from './ReactImg';
import MathComp from './MathComp';
import BasicAccount from './BasicAccount';
import AccountsComp from './AccountsComp';

import Reactimg from './Reactimg.png';
import Mathematicsimg from './Mathematicsimg.png';
import Moneyimg from './Moneyimg.png';
import Accountimg from './Accountimg.jpeg';
import Globeimg from './Globeimg.jpeg';

class Header extends React.Component {
	constructor() {
		super()
		this.state = {
			greeting: "Hello World",
			display: null,
		}
		this.handleClick = this.handleClick.bind(this);
	}

	handleClick(e) {
		if(e.target.id === "reactimg") {
			this.setState({								//shorthand for setting state, instead of function
				greeting: 'You clicked the React icon',
				display: <ReactImg />
			})
		} else if (e.target.id === "mathimg") {
			this.setState({
				greeting: 'You clicked the MathComp icon',
				display: <MathComp />
			})
		} else if (e.target.id === "moneyimg") {
			this.setState({
				greeting: 'You clicked the AccountComp icon',
				display: <BasicAccount />
			}) 
		} else if (e.target.id === "accountimg") {
			this.setState({
				greeting: 'You clicked the AccountsComp icon',
				display: <AccountsComp />
			})
		} else if (e.target.id === "globeimg") { 
			this.setState({
				greeting: 'You clicked the Globe icon',
				display: null
			})
		}			
	}

	render() {
		return(
			<div>
				<header>
					<h1>{this.state.greeting}</h1>
					<img onClick={this.handleClick} src={Reactimg} alt="reactimg" id="reactimg" className="icons"></img>
					<img onClick={this.handleClick} src={Mathematicsimg} alt="mathimg" id="mathimg" className="icons"></img>
					<img onClick={this.handleClick} src={Moneyimg} alt="moneyimg" id="moneyimg" className="icons"></img>
					<img onClick={this.handleClick} src={Accountimg} alt="accountimg" id="accountimg" className="icons"></img>
					<img onClick={this.handleClick} src={Globeimg} alt="globeimg" id="globeimg" className="icons"></img>
				</header>
				<div className = "display">
					{this.state.display}
				</div>
			</div>
		)
	}

}

export default Header;