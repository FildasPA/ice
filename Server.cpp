#include <Ice/Ice.h>
#include <Coll.h>

using namespace std;
using namespace TP;

class CollI : public Coll
{
private:
	//TP::Collection collection;
	//virtual void addTrack(const TP::Track& t);
	//virtual void addTracks();
public:
	//virtual void add(const TP::Track& t, const Ice::Current&);
	//virtual void remove(const TP::Track& t, const Ice::Current&);
	//virtual TP::Collection search(const TP::Track& t, const Ice::Current&);
	//virtual TP::Collection searchForTrackByAuthor(const string& s, const Ice::Current&);
	//virtual TP::Collection searchForTrackByTitle(const string& s, const Ice::Current&);

	virtual TP::Track getTrack(const Ice::Current&);
};

/*void
CollI::
add(const TP::Track* t, const Ice::Current&)
{
	std::cout << "Add track: " << t.author << " - " << t.title << std::endl;
	addTrack(t);
}

void
CollI::
remove(const TP::Track& t, const Ice::Current&)
{
	std::cout << "Remove track: " << t.author << " - " << t.title << std::endl;
	for (TP::Collection::iterator it = CollI::collection.begin() ; it != CollI::collection.end();) {
		if ((!t.author.empty() && it->author == t.author && t.title.empty()) ||
		    (!t.author.empty() && it->author == t.author && !t.title.empty() && it->title == t.title) ||
		    (t.author.empty() && !t.title.empty() && it->title == t.title)) {
			it = CollI::collection.erase(it);
		} else {
			++it;
		}
	}
}

TP::Collection
CollI::
search(const TP::Track& t, const Ice::Current&)
{
	TP::Collection c;

	for (TP::Collection::iterator it = CollI::collection.begin() ; it != CollI::collection.end(); ++it) {
		if ((t.author.empty() && t.title.empty()) ||
		    (!t.author.empty() && it->author.find(t.author) != std::string::npos && t.title.empty()) ||
		    (!t.author.empty() && it->author.find(t.author) != std::string::npos && !t.title.empty() && it->title.find(t.title) != std::string::npos) ||
		    (t.author.empty() && !t.title.empty() && it->title.find(t.title) != std::string::npos)) {
			c.push_back(*it);
		}
	}

	return c;
}

TP::Collection
CollI::
searchForTrackByAuthor(const string& s, const Ice::Current&)
{
	TP::Collection c;

	for (TP::Collection::iterator it = CollI::collection.begin() ; it != CollI::collection.end(); ++it) {
		if (it->author.find(s) != std::string::npos) {
			c.push_back(*it);
		}
	}

	return c;
}

TP::Collection
CollI::
searchForTrackByTitle(const string& s, const Ice::Current&)
{
	TP::Collection c;

	for (TP::Collection::iterator it = CollI::collection.begin() ; it != CollI::collection.end(); ++it) {
		if (it->title.find(s) != std::string::npos) {
			c.push_back(*it);
		}
	}

	return c;
}*/

TP::Track CollI::getTrack(const Ice::Current&)
{
	TP::Track t1;
	t1.author = "Muse";
	t1.title = "Undisclosed Desires";
	t1.filePath = "/home/etudiants/inf/uapv1502198/s2/muse.mp3";
	t1.length = 236;
	return t1;
}

//-----------------------------------------------------------------------------
// * Add track
//-----------------------------------------------------------------------------
//void CollI::addTrack(const TP::Track& t)
//{
//	CollI::collection.push_back(t);
//}

//-----------------------------------------------------------------------------
// * Add tracks
//-----------------------------------------------------------------------------
//void CollI::addTracks()
//{
//	Track* t1 = new Track();
//	t1->author = "Muse";
//	t1->title = "Undisclosed Desires";
//	t1->filePath = "/home/etudiants/inf/uapv1502198/s2/muse.mp3";
//	t1->duration = 236;
//	addTrack(t1);
//}




int
main(int argc, char* argv[])
{

	int status = 0;
	Ice::CommunicatorPtr ic;
	try {
		ic = Ice::initialize(argc, argv);
		Ice::ObjectAdapterPtr adapter =
		  ic->createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000");
		Ice::ObjectPtr object = new CollI;
		adapter->add(object, ic->stringToIdentity("SimplePrinter"));

		//addTracks();

		adapter->activate();
		ic->waitForShutdown();
	} catch (const Ice::Exception& e) {
		cerr << e << endl;
		status = 1;
	} catch (const char* msg) {
		cerr << msg << endl;
		status = 1;
	}
	if (ic) {
		try {
			ic->destroy();
		} catch (const Ice::Exception& e) {
			cerr << e << endl;
			status = 1;
		}
	}
	return status;
}
