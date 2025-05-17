server:
	@echo "start MCP server on http://localhost:8000/docs"
	uv run main.py

clean:
	@echo "clean python dependencies..."
	rm -rf .venv
	rm -rf venv
	rm -rf __pycache__/
	rm -f uv.lock
	@echo "clean successful...!"
	
