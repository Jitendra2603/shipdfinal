"use client";

import { useState, useEffect } from "react";
import CodeEditor from "./components/CodeEditor";

export default function Home() {
  const [filter, setFilter] = useState("");

  useEffect(() => {
    const handleInteraction = () => {
      setFilter("blur(6px) grayscale(100%)");
    };

    window.addEventListener("click", handleInteraction);
    window.addEventListener("keydown", handleInteraction);

    return () => {
      window.removeEventListener("click", handleInteraction);
      window.removeEventListener("keydown", handleInteraction);
    };
  }, []);

  return (
    <main className="flex h-screen flex-col items-center justify-self-start p-24 relative">
      <video
        src="/video/wave-loop.mp4"
        poster="/video/wave-loop.jpg"
        autoPlay
        loop
        muted
        className="h-full w-full object-cover fixed top-0 left-0"
        style={{
          filter,
          transition: "filter 1s ease-in-out",
          zIndex: -1,
        }}
      ></video>
      <div className="w-full items-center justify-center font-mono bg-white relative z-10">
        <h1 className="w-full text-2xl font-semibold pl-2 text-black" style={{ marginTop: '-60px' }}>
          Datacurve 
        </h1>
      </div>
      <CodeEditor />
    </main>
  );
}
