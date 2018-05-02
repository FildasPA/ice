module Vocal
{
	struct Track
	{
		string author;
		string title;
		string filepath;
		int duration;
	};

	sequence<Track> Collection;

	interface Coll
	{
		void add(Track t);
		Collection search(Track t);
		string startStream(Track t);
		string searchTrackAndStream(Track t);
		void pauseStream();
		void resumeStream();
		void stopStream();
	};
};
