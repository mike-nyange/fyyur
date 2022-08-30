from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue_Genre(db.Model):
    __tablename__ = "venue_genres"
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(
        db.Integer, db.ForeignKey("venues.id", ondelete="CASCADE"), nullable=False
    )
    genre = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Venue Genre:{self.genre}"

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120))
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres =  genres = db.relationship(
        "Venue_Genre", backref="venue", lazy=True,
    )
    website_link = db.Column(db.String(255), nullable=True)
    seeking_talent = db.Column(db.Boolean, nullable=True, default=False)
    seeking_description = db.Column(db.String(120), nullable=True)
    show = db.relationship('Show', backref='venue', lazy=True)
    
    def __repr__(self):
           return f'Venue: {self.name}'

class Artist_Genre(db.Model):
    __tablename__ = "artist_genres"
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    genre = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Artist Genre: {self.genre}>"



class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.relationship("Artist_Genre", backref="artist", lazy=True)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website_link = db.Column(db.String(255))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(), nullable=False)
    show = db.relationship('Show', backref='artist', lazy=True)
    #venues = db.relationship(
     #   "Venue", secondary="shows", backref=db.backref("artists", lazy=True)
    #)
    
    def __repr__(self):
          return f'Artist: {self.name}'

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    #setting up foreign key constraint linking to the Artist parent model
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False )
    #setting up foreign key constraint linking to the Venue parent model
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False )
    start_time = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
             return f'{self.artist_id}\'s show at {self.venue_id}'

