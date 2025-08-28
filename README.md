# 🧠 Neurobloom Pact Contract Testing

> **Crystal clear contract testing for AI services** 💎  
> Professional-grade testing framework ensuring bulletproof API contracts

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-passing-green.svg)](https://github.com/neurobloomai/pact-contract-testing/actions)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🚀 What is This?

**Contract testing for AI services** - ensuring your neurobloom.ai APIs work perfectly across all environments (K1, K2, K3... K∞!). 

Built with **separation of concerns** in mind, this repo focuses purely on **contract testing** using the [Pact framework](https://docs.pact.io/), while our main [PACT Protocol](https://github.com/neurobloomai/pact) handles agent collaboration.

### 🎯 Key Features

- ✅ **HTTP Client Testing** - Real network communication validation
- ✅ **Mock Server Integration** - Flask-based testing infrastructure  
- ✅ **Contract Generation** - Automated Pact file creation
- ✅ **OpenAI Integration** - AI analysis service testing
- ✅ **Multi-Environment Ready** - Works across all deployment targets
- ✅ **Professional Structure** - Clean separation of concerns

## ⚡ Quick Start

```bash
# Clone the repo
git clone https://github.com/neurobloomai/pact-contract-testing.git
cd pact-contract-testing

# Install dependencies
pip install -r requirements.txt

# Run the demo (see it work in 30 seconds!)
python docs/examples/demo.py

# Run all tests
pytest tests/ -v
```

**That's it!** You should see:
```
🧠 Neurobloom AI Analysis Demo
====================================
🚀 Mock server started on http://127.0.0.1:8082
🏥 Health Check...
   Status: healthy
📊 Testing time_series analysis...
   Confidence: 0.87
   Insights (3):
     1. Key pattern identified in time_series data
     2. Strong correlation detected between variables
     3. Seasonal trend observed with 95% confidence
✅ Demo completed!
```

## 📂 Project Structure

```
pact-contract-testing/
├── src/neurobloom/              # Core source code
│   ├── client.py               # HTTP client for AI service
│   ├── service.py              # OpenAI integration service
│   └── models.py               # Request/response models
├── tests/                       # Comprehensive test suite
│   ├── unit/                   # Unit tests
│   ├── integration/            # HTTP integration tests
│   └── contract/               # Pact contract tests
│       ├── consumer/           # Consumer contract tests
│       └── provider/           # Provider verification
├── pact-contracts/             # Generated contract files
├── scripts/                    # Utility scripts
│   ├── start_mock_server.py    # Standalone mock server
│   └── run_contract_tests.sh   # Test automation
└── docs/examples/              # Usage examples
```

## 🧪 Testing Approach

### Unit Tests
```bash
# Test data models and core logic
pytest tests/unit/ -v
```

### Integration Tests  
```bash
# Test real HTTP communication with mock server
pytest tests/integration/ -v
```

### Contract Tests (Coming Soon!)
```bash
# Generate and verify Pact contracts
pytest tests/contract/ -v
```

## 🔧 Usage Examples

### Basic AI Analysis Client

```python
from src.neurobloom.client import NeuroBloomClient
from src.neurobloom.models import AnalysisRequest

# Create client
client = NeuroBloomClient('https://api.neurobloom.ai')

# Prepare analysis request
request = AnalysisRequest(
    data=[
        {"timestamp": "2024-01-01", "sales": 1200},
        {"timestamp": "2024-01-02", "sales": 1350}
    ],
    analysis_type="sales_forecasting",
    model="gpt-4"
)

# Get AI insights
result = client.analyze_data(request)
print(f"Confidence: {result.confidence_score}")
for insight in result.insights:
    print(f"💡 {insight}")
```

### Mock Server for Development

```python
# Start mock server for testing
python scripts/start_mock_server.py 8080

# Or programmatically
from tests.integration.mock_server import MockNeuroBloomServer

server = MockNeuroBloomServer(port=8080)
server.start()
# ... your tests ...
server.stop()
```

## 🎯 Analysis Types Supported

| Type | Description | Confidence | Use Case |
|------|-------------|------------|----------|
| `time_series` | Trend analysis and forecasting | 0.87 | Sales, metrics, IoT data |
| `classification` | Pattern recognition and clustering | 0.92 | Data categorization, ML |  
| `sales_forecasting` | Revenue prediction and insights | 0.78 | Business planning, growth |

## 🚀 Development

### Running Tests

```bash
# All tests with coverage
./scripts/run_contract_tests.sh

# Specific test types
pytest tests/unit/ -v                    # Unit tests only
pytest tests/integration/ -v             # Integration tests only
pytest tests/contract/consumer/ -v       # Consumer contracts
pytest tests/contract/provider/ -v       # Provider verification

# With coverage report
pytest --cov=src --cov-report=html tests/
```

### Mock Server Development

```bash
# Start standalone mock server
python scripts/start_mock_server.py 8080

# Test endpoints
curl http://localhost:8080/health
curl -X POST http://localhost:8080/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{"data": [{"test": "value"}], "analysis_type": "time_series"}'
```

## 🏗️ Architecture Philosophy

This project follows **separation of concerns**:

- **`src/neurobloom/client.py`** → Clean HTTP client interface
- **`src/neurobloom/service.py`** → OpenAI integration logic  
- **`src/neurobloom/models.py`** → Data structures and validation
- **`tests/integration/`** → Real HTTP testing
- **`tests/contract/`** → Contract testing with Pact framework
- **`scripts/`** → Development utilities

**Why This Matters:**
- ✅ **Easy to test** individual components
- ✅ **Clear responsibilities** for each module
- ✅ **Maintainable codebase** as complexity grows
- ✅ **Professional standards** for enterprise deployment

## 🤝 Contributing

We welcome contributions! This is a **public repository** showcasing professional contract testing practices.

### Getting Started

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Make your changes** (follow our structure!)
4. **Add tests:** Ensure new features have corresponding tests
5. **Run the test suite:** `./scripts/run_contract_tests.sh`
6. **Submit a Pull Request**

### Good First Issues

- [ ] Add more analysis types (`sentiment_analysis`, `anomaly_detection`)
- [ ] Implement full Pact contract tests in `tests/contract/`
- [ ] Add performance benchmarking
- [ ] Create Docker Compose setup for easy development
- [ ] Add CI/CD pipeline with GitHub Actions

### Code Standards

- **Python 3.9+** required
- **Black** for code formatting: `black src/ tests/`
- **Pytest** for all tests
- **Type hints** encouraged
- **Clear documentation** for public APIs

## 📋 Roadmap

### Phase 1: Foundation ✅
- [x] Project structure and organization
- [x] HTTP client implementation  
- [x] Mock server for testing
- [x] Unit and integration tests
- [x] Professional documentation

### Phase 2: Contract Testing 🚧
- [ ] Full Pact consumer tests
- [ ] Provider verification setup
- [ ] Contract file generation
- [ ] Multi-environment contract validation

### Phase 3: Advanced Features 🔮
- [ ] Real OpenAI integration
- [ ] Performance testing
- [ ] Load balancer testing
- [ ] Multi-region deployment contracts
- [ ] Automated contract publishing

## 🔗 Related Projects

- **[neurobloomai/pact](https://github.com/neurobloomai/pact)** - PACT Protocol for Agent Collaboration
- **[Pact Foundation](https://docs.pact.io/)** - Contract testing framework
- **[OpenAI API](https://platform.openai.com/docs)** - AI model integration

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

## 💬 Support & Discussion

- **Issues:** [GitHub Issues](https://github.com/neurobloomai/pact-contract-testing/issues)
- **Discussions:** [GitHub Discussions](https://github.com/neurobloomai/pact-contract-testing/discussions) 
- **Email:** [founders@neurobloom.ai](mailto:founders@neurobloom.ai)

## 🌟 Why Contract Testing Matters

> *"Testing is about confidence. Contract testing gives you confidence that your services will work together, without the complexity and brittleness of end-to-end tests."*

**Traditional Integration Testing:**
- 🔴 Slow and expensive
- 🔴 Flaky and hard to debug
- 🔴 Requires full environment setup
- 🔴 Breaks frequently in CI/CD

**Contract Testing with Pact:**
- 🟢 Fast unit-test speed
- 🟢 Reliable and deterministic
- 🟢 Isolated testing
- 🟢 Clear failure messages

---

**Built with 💎 by [NeuroBloom AI](https://neurobloom.ai)**  
*Making AI service testing crystal clear, one contract at a time.*
