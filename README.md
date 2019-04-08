**Purpose**
===========

To allow extraction of class and function comments 
and output to Sphinx compatible rst files for later inclusion in Sphinx docs.


**Go**
------

Both block and line comments are supported. Comments like the following are supported:

    /*
    |  e12  |
    |   | \ |
    |  s10 e20
    |   | / |
    |   /   |
    | / |   |
    s00 |  s20
    |   |   |
    e01 |   |
    | \ |   |
    e0  e1  e2
    |   |   |
    r0  r1  r2
    0   1   2
    */
    func initPoset(t *testing.T) (*Poset, map[string]EventHash) {

Embedded rst:

    /*
    .. raw:: html
    
    	<object data="../../_images/graphviz.svg" type="image/svg+xml"></object>
    */
    func initConsensusPoset(db bool, t testing.TB) (*Poset, map[string]EventHash) {

and multi-line:

    // Format implements fmt.Formatter, forcing the byte slice to be formatted as is,
    // without going through the stringer interface used for logging.
    func (a Address) Format(s fmt.State, c rune) {

**Java**
--------

Java doc strings are supported. Comments like the following are supported:
 
    /**
     * Test for Poset
     * @author qn
     *
     */
    public class PosetTest {
    

**Rust**
--------

Java doc strings are supported, same as in Java:

    /**
      * extra long function declaration
      */
    fn _get_ancestors<'a>(
        graph: &'a BTreeHashgraph,
        id: &'a EventHash,
        parent_pair_elem: ParentPairElem,
    ) -> Result<Vec<&'a EventHash>, Error> {