import React from "react";
import { render, fireEvent, screen, waitFor } from "@testing-library/react";
import CodeEditor from "../app/components/CodeEditor";
import "@testing-library/jest-dom/extend-expect";

describe("CodeEditor Component", () => {
  test("renders without crashing", () => {
    render(<CodeEditor />);
    const editorElement = screen.getByRole("textbox");
    expect(editorElement).toBeInTheDocument();
  });

  test("syntax highlighting works", () => {
    render(<CodeEditor />);
    const editorElement = screen.getByRole("textbox");
    fireEvent.change(editorElement, { target: { value: 'print("Hello World")' } });
    expect(editorElement).toHaveValue('print("Hello World")');
  });

  test("run code button triggers code execution and displays output", async () => {
    render(<CodeEditor />);
    const runButton = screen.getByText("Run Code");
    fireEvent.click(runButton);
    const outputArea = await waitFor(() =>
      screen.getByPlaceholderText("Output will be displayed here")
    );
    expect(outputArea).toHaveValue("Hello, World!\n");
  });
});
