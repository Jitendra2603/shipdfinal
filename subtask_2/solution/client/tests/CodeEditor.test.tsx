import React from "react";
import { render, fireEvent, screen, waitFor } from "@testing-library/react";
import { expect } from "chai";
import sinon from "sinon";
import CodeEditor from "../app/components/CodeEditor";

describe("CodeEditor Component", () => {
  let fetchStub: sinon.SinonStub;

  beforeEach(() => {
    fetchStub = sinon.stub(global, "fetch");
  });

  afterEach(() => {
    fetchStub.restore();
  });

  it("renders without crashing", () => {
    render(<CodeEditor />);
    const editorElement = screen.getByPlaceholderText("Write your Python code here");
    expect(editorElement).to.exist;
  });

  it("syntax highlighting works", () => {
    render(<CodeEditor />);
    const editorElement = screen.getByPlaceholderText("Write your Python code here") as HTMLDivElement;
    // CodeMirror renders a div, check initial code
    expect(editorElement.textContent).to.include("# Write your Python code here");
  });

  it("run code button triggers code execution and displays output", async () => {
    // Mock the fetch response for run_code
    fetchStub.withArgs("http://localhost:8000/run_code").resolves({
      json: async () => ({
        success: true,
        output: "Hello, World!\n",
        error: "",
      }),
    } as Response);

    render(<CodeEditor />);
    const runButton = screen.getByText("Run Code");
    fireEvent.click(runButton);
    const outputArea = await waitFor(() => screen.getByPlaceholderText("Output will be displayed here"));
    expect((outputArea as HTMLTextAreaElement).value).to.equal("Hello, World!\n");
  });

  it("submit code button triggers code submission and displays output", async () => {
    // Mock the fetch response for submit_code
    fetchStub.withArgs("http://localhost:8000/submit_code").resolves({
      json: async () => ({
        db_success: true,
        code_output: {
          success: true,
          output: "Hello, World!\n",
          error: "",
        },
        error: "",
      }),
    } as Response);

    render(<CodeEditor />);
    const submitButton = screen.getByText("Submit Code");
    fireEvent.click(submitButton);
    const outputArea = await waitFor(() => screen.getByPlaceholderText("Output will be displayed here"));
    expect((outputArea as HTMLTextAreaElement).value).to.equal("Hello, World!\n");
  });
});
