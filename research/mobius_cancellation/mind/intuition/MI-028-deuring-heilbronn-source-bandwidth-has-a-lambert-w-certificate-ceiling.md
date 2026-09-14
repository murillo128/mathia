# MI-028 — Deuring--Heilbronn source bandwidth has a Lambert-W certificate ceiling

**Evidence level:** literature-backed zero repulsion plus exact parameter inversion from [MC-300](../../findings/MC-300-deuring-heilbronn-lambert-w-source-band-envelope.md)

For a Page-shell target embedded with one exceptional real character, let `delta_*` be the exceptional zero distance from `1`, `v=log q` the common-modulus cost, and `L_1=log y`, `L_2=log log y`. The explicit Deuring--Heilbronn route certifies any fixed inverse-log shell accuracy only while

`v ≲_A (L_1/L_2) W(c_A L_2/(delta_* L_1))`.

The Lambert `W` is not a convenient reparametrization: it is forced by balancing the logarithmic repulsion numerator against the conductor in its denominator. With only the coarse exceptional-zero information `delta_* ≲ 1/(L_1 L_2)`, the worst admissible case gives the uniform scale

`log q = O_A(L_1 log log log y / L_2)`.

Thus the `log log log y` enlargement found in MC-299 is the natural information limit of this **particular certificate with this particular input**. Retuning truncation heights or constants cannot produce a parametrically wider uniform band without new arithmetic information.

The boundary is methodological, not an impossibility theorem about the characters or zeros themselves. A substantially smaller actual `delta_*`, a collective zero-density/source-capacity argument, or a different arithmetic carrier can widen the accessible family. The reusable lesson is to distinguish a theorem's source-band ceiling from a true nonexistence statement: once the black-box inequality has been inverted, further progress must change an input or mechanism rather than optimize constants inside the same channel.
