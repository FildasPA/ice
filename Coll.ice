module Vocal
{
	struct Track
	{
		string author;
		string title;
		string filePath;
		int duration;
	};

	sequence<Track> Collection;

	interface Coll
	{
		void add(Track t);
		void remove(Track t);
		Collection search(Track t);
		Track getTrack(Track t);
	};
};
