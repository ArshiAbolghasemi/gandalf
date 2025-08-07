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

## Usage Examples

### Create a new itinerary
Submit an itinerary request and receive a job ID for tracking:

```bash
curl -X POST http://localhost:8000/api/v1/itineraries \
  -H "Content-Type: application/json" \
  -d '{"destination": "Barcelona", "durationDays": 3}'
```

**Response:**
```json
{"jobId":"c86b0cf8-ba5e-4fdd-97f5-f9dc3266f782"}
```

### Check itinerary status
Poll the endpoint with the job ID to check completion status and retrieve the generated itinerary:

```bash
curl -X GET http://localhost:8000/api/v1/itineraries/c86b0cf8-ba5e-4fdd-97f5-f9dc3266f782 \
  -H "Content-Type: application/json"
```

**Response:**
```json
{
  "document": {
    "jobId": "c86b0cf8-ba5e-4fdd-97f5-f9dc3266f782",
    "status": "completed",
    "destination": "Barcelona",
    "durationDays": 3,
    "createdAt": "2025-08-07T14:01:18.810282Z",
    "completedAt": "2025-08-07T14:01:33.759936Z",
    "itinerary": [
      {
        "day": 1,
        "theme": "Historic Barcelona",
        "activities": [
          {
            "time": "Morning",
            "description": "Explore the Gothic Quarter: Wander through the medieval streets, admire the architecture, visit the Barcelona Cathedral, and enjoy the Plaça Reial.",
            "location": "Gothic Quarter (Barri Gòtic), Barcelona"
          },
          {
            "time": "Afternoon",
            "description": "Tour the Picasso Museum: Discover the iconic works of Pablo Picasso in one of the world's foremost Picasso collections.",
            "location": "Museu Picasso, Carrer Montcada 15-23, Barcelona"
          }
        ]
      },
      {
        "day": 2,
        "theme": "Gaudí and Modernisme",
        "activities": [
          {
            "time": "Morning",
            "description": "Visit Sagrada Família: Marvel at Antoni Gaudí's masterpiece, the famous basilica with breathtaking architecture and stained glass.",
            "location": "Sagrada Família, Carrer de Mallorca, 401, Barcelona"
          },
          {
            "time": "Afternoon",
            "description": "Stroll through Park Güell: Enjoy colorful mosaics, whimsical structures, and panoramic views over Barcelona in this enchanting park designed by Gaudí.",
            "location": "Park Güell, Carrer d'Olot, Barcelona"
          }
        ]
      },
      {
        "day": 3,
        "theme": "Seaside and Local Life",
        "activities": [
          {
            "time": "Morning",
            "description": "Relax at Barceloneta Beach: Enjoy the sun, Mediterranean sea, and a paseo along the promenade. Try a seaside coffee at a chiringuito (beach bar).",
            "location": "Barceloneta Beach, Barcelona"
          },
          {
            "time": "Afternoon",
            "description": "Explore La Boqueria Market and Ramblas: Wander through the iconic market to sample local foods and juices, then stroll along Las Ramblas to experience street life and local shops.",
            "location": "La Boqueria Market, La Rambla, 91, Barcelona"
          }
        ]
      }
    ],
    "error": null
  }
}
```

## How to Run
Copy `.env.example` to `.env` and configure the required environment variables
Then build the project
```bash
docker-compose up -d --build
```

## Processing Flow
1. Client submits itinerary request via POST endpoint
2. System generates unique job ID and stores initial document in Firestore
3. Background task processes request using OpenAI API
4. Client polls GET endpoint to check completion status
5. Generated itinerary is returned when processing completes

Wiki pages you might want to explore for more details:
- [Wiki Page](https://deepwiki.com/ArshiAbolghasemi/gandalf)
