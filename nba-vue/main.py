from fastapi import FastAPI
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NBA API Backend"}

@app.get("/teams")
def get_teams():
    """Fetches a list of NBA teams with image URLs"""
    team_images = {
        1610612737: "https://cdn.nba.com/logos/nba/1610612737/primary/L/logo.svg",  # Atlanta Hawks
        1610612738: "https://cdn.nba.com/logos/nba/1610612738/primary/L/logo.svg",  # Boston Celtics
        1610612739: "https://cdn.nba.com/logos/nba/1610612739/primary/L/logo.svg",  # Cleveland Cavaliers
        1610612740: "https://cdn.nba.com/logos/nba/1610612740/primary/L/logo.svg",  # New Orleans Pelicans
        1610612741: "https://cdn.nba.com/logos/nba/1610612741/primary/L/logo.svg",  # Chicago Bulls
        1610612742: "https://cdn.nba.com/logos/nba/1610612742/primary/L/logo.svg",  # Dallas Mavericks
        1610612743: "https://cdn.nba.com/logos/nba/1610612743/primary/L/logo.svg",  # Denver Nuggets
        1610612744: "https://cdn.nba.com/logos/nba/1610612744/primary/L/logo.svg",  # Golden State Warriors
        1610612745: "https://cdn.nba.com/logos/nba/1610612745/primary/L/logo.svg",  # Houston Rockets
        1610612746: "https://cdn.nba.com/logos/nba/1610612746/primary/L/logo.svg",  # Los Angeles Clippers
        1610612747: "https://cdn.nba.com/logos/nba/1610612747/primary/L/logo.svg",  # Los Angeles Lakers
        1610612748: "https://cdn.nba.com/logos/nba/1610612748/primary/L/logo.svg",  # Miami Heat
        1610612749: "https://cdn.nba.com/logos/nba/1610612749/primary/L/logo.svg",  # Milwaukee Bucks
        1610612750: "https://cdn.nba.com/logos/nba/1610612750/primary/L/logo.svg",  # Minnesota Timberwolves
        1610612751: "https://cdn.nba.com/logos/nba/1610612751/primary/L/logo.svg",  # Brooklyn Nets
        1610612752: "https://cdn.nba.com/logos/nba/1610612752/primary/L/logo.svg",  # New York Knicks
        1610612753: "https://cdn.nba.com/logos/nba/1610612753/primary/L/logo.svg",  # Orlando Magic
        1610612754: "https://cdn.nba.com/logos/nba/1610612754/primary/L/logo.svg",  # Indiana Pacers
        1610612755: "https://cdn.nba.com/logos/nba/1610612755/primary/L/logo.svg",  # Philadelphia 76ers
        1610612756: "https://cdn.nba.com/logos/nba/1610612756/primary/L/logo.svg",  # Phoenix Suns
        1610612757: "https://cdn.nba.com/logos/nba/1610612757/primary/L/logo.svg",  # Portland Trail Blazers
        1610612758: "https://cdn.nba.com/logos/nba/1610612758/primary/L/logo.svg",  # Sacramento Kings
        1610612759: "https://cdn.nba.com/logos/nba/1610612759/primary/L/logo.svg",  # San Antonio Spurs
        1610612760: "https://cdn.nba.com/logos/nba/1610612760/primary/L/logo.svg",  # Oklahoma City Thunder
        1610612761: "https://cdn.nba.com/logos/nba/1610612761/primary/L/logo.svg",  # Toronto Raptors
        1610612762: "https://cdn.nba.com/logos/nba/1610612762/primary/L/logo.svg",  # Utah Jazz
        1610612763: "https://cdn.nba.com/logos/nba/1610612763/primary/L/logo.svg",  # Memphis Grizzlies
        1610612764: "https://cdn.nba.com/logos/nba/1610612764/primary/L/logo.svg",  # Washington Wizards
        1610612765: "https://cdn.nba.com/logos/nba/1610612765/primary/L/logo.svg",  # Detroit Pistons
        1610612766: "https://cdn.nba.com/logos/nba/1610612766/primary/L/logo.svg",  # Charlotte Hornets
    }

    team_list = teams.get_teams()
    for team in team_list:
        team["image_url"] = team_images.get(team["id"], "https://via.placeholder.com/150")  # Placeholder image

    return {"teams": team_list}

@app.get("/games/{team_id}")
def get_games(team_id: int):
    """Fetches games played by a specific team"""
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0].to_dict(orient="records")
    return {"games": games}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust origins if needed
    allow_methods=["*"],
    allow_headers=["*"],
)