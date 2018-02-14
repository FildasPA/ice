module TP
{
	struct Track
	{
		string author;
		string title;
		string filePath;
		int length;
	};

	//sequence<Track> Collection;

	interface Coll
	{
		//void add(Track t);
		//void remove(Track t);
		//Collection search(Track t);
		//Collection searchForTrackByAuthor(string name);
		//Collection searchForTrackByTitle(string name);

		Track getTrack();
	};
};
