const { spawn } = require('child_process');
const path = require('path');

let server;

exports.handler = async (event, context) => {
  // Only start server once
  if (!server) {
    const pythonProcess = spawn('python', [
      '-m', 'flask', 'run',
      '--host', '0.0.0.0',
      '--port', '5000'
    ], {
      cwd: path.join(__dirname, '..'),
      stdio: 'pipe'
    });

    server = pythonProcess;
  }

  // Proxy request to Flask
  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Flask app is running' })
  };
};
