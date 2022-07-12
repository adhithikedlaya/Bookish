import React, { Component } from "react";
import {
  LandingDiv,
  LandingTitleTag,
  LandingTitleContainer,
} from "./NotLandingPage";

export class LandingPage extends Component {
  constructor(props) {
    super(props);

    this.state = {example: props.example};
  }

  render() {
    return (
      <LandingDiv>
        <LandingTitleContainer>
          <LandingTitleTag>Helloooo</LandingTitleTag>
          <li>{this.props.okStatus}!</li>
        </LandingTitleContainer>
      </LandingDiv>
    );
  }
}
