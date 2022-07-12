import React, { useState } from "react";
import { Container } from "reactstrap";
import { LandingPage } from "./LandingPage";
import { ApiService } from "./ApiService";
import { TestPage } from "./TestPage";

export default function App() {
  const apiService = new ApiService()
  const [state, setState] = useState(BLANK_STATE);

  let healthCheck = () => {
    apiService.healthCheck().then((status) => {
      initialize(status);
    });
  };

  let initialize = (status) => {
    setState(status);
  };

  if (state === BLANK_STATE) {
    healthCheck()
  }

  return (
    <div>
      <Container>
          <LandingPage okStatus={state.status}/>
      </Container>

      <Container>
          <TestPage okStatus={state.status}/>
      </Container>
    </div>
  );
}

const BLANK_STATE = {
  status: ""
};
