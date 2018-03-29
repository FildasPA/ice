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
		Collection search(Track t);
		Track streamTrack(Track t);
	};
};
