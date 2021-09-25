import React from "react";
import useForm from "./useForm";
const Form = () => {
  const register = (values) => {
    console.log(values);
  };
  const [values, handleChange, handleSubmit] = useForm();
  return (
    <form onSubmit={handleSubmit(register)}>
      <label>Name:</label>
      <input
        value={values.name || ""}
        onChange={handleChange}
        name="name"
        type="text"
      />
      <label>handle:</label>
      <input
        value={values.handle || ""}
        onChange={handleChange}
        name="handle"
        type="text"
      />
      <label>boos:</label>
      <input
        value={values.boos || ""}
        onChange={handleChange}
        name="boos"
        type="text"
      />
      <button type="submit">Register</button>
    </form>
  );
};

export default Form;
