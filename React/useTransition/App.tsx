import { useState } from "react";
import { useTransition } from "./useTransition";

function App() {
  const [isMounted, setIsMounted] = useState(false);
  const { stylesTransition, shouldRender } = useTransition(isMounted, 500, {
    from: { width: 100, opacity: 0 },
    to: { width: 300, opacity: 1 },
  });
  return (
    <div className="App">
      {shouldRender && (
        <div style={{ ...stylesTransition, background: "red" }}>
          <h1>salalas</h1>
        </div>
      )}
      <button onClick={() => setIsMounted((prev) => !prev)}>Click me!</button>
    </div>
  );
}

export default App;
