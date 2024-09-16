// jest.config.js
const nextJest = require("next/jest");

const createJestConfig = nextJest({
  dir: "./",
});

const customJestConfig = {
  setupFilesAfterEnv: ["solution/client/jest.setup.js"],
  testEnvironment: "jsdom",
  testMatch: ["solution/client/tests/**/*.test.(js|jsx|ts|tsx)"], // Include the tests folder
};

module.exports = createJestConfig(customJestConfig);
