# gandalf
Gandalf is an AI travel planner that generates itineraries. making trip planning effortless and enjoyable.

## Features

- **Asynchronous Processing**: Submit itinerary requests and poll for completion
- **AI-Powered Generation**: Uses OpenAI models to create detailed travel plans
- **Cloud Storage**: Persists itineraries in Google Cloud Firestore
- **RESTful API**: Clean REST endpoints with proper error handling

## API Endpoints

For complete API documentation with interactive examples, visit the Swagger UI at:
```
http://localhost:8000/docs#/
```

## Configuration

Copy `.env.example` to `.env` and configure the required environment variables: <cite/>

## Processing Flow

1. Client submits itinerary request via POST endpoint
2. System generates unique job ID and stores initial document in Firestore
3. Background task processes request using OpenAI API
4. Client polls GET endpoint to check completion status
5. Generated itinerary is returned when processing completes

Wiki pages you might want to explore for more details:
- [Wiki Page](https://deepwiki.com/ArshiAbolghasemi/gandalf)
