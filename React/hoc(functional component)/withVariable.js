import React from "react";

const withVariable = (WrappedComponent) => (props) => {
  const greeting = "hello";

  return <WrappedComponent {...props} greeting={greeting} />;
};

export default withVariable;
