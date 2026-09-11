# MI-025 — Regular sampling separates aliasing, joint coupling, and finite-window stability

**Evidence level:** supported by the exact phase-pushforward classifications and recurrence constructions in AF-279--AF-280; restricted to the stated absolutely convergent ordinary-Dirichlet coefficient class.

For

\[
F(s)=\sum_n a_n n^{-s},\qquad \sum_n |a_n|n^{-c}<\infty,
\]

a regular vertical lattice `c+ikh` retains the pushed phase `n -> e^{-ih\log n}`, not the frequency `\log n` itself. With

\[
R_h=\{r\in\mathbb Q_{>0}:h\log r\in2\pi\mathbb Z\},
\]

AF-279 gives exact coefficient fidelity for the complete bilateral lattice iff `R_h={1}`.

AF-280 shows that finitely many such lattices do **not** combine several lossy quotients into a faithful one. If every cadence `h_j` has a nontrivial rational resonance `r_j`, the finite group-algebra element

\[
P=\prod_j(1-[r_j])
\]

produces a nonzero finite-support Dirichlet perturbation annihilated by every lattice. Hence

\[
\mathcal S_{(h_1,\ldots,h_J)}\text{ injective}
\iff
R_{h_j}=\{1\}\text{ for at least one }j.
\]

The obstruction is stronger than failure of the combined phase labels. Two cadences can give an injective tuple `n -> (e^{-ih_1\log n},e^{-ih_2\log n})` while the acquisition still loses the interaction because it observes the complete one-coordinate sample sequences separately rather than the joint phase law. The four-term `{N,2N,3N,6N}` alternating cycle for `h_1=2\pi/\log2`, `h_2=2\pi/\log3` is the exact model.

Even when one cadence is nonresonant and the infinite channel is injective, every preassigned finite family of windows remains nonuniformly conditioned on the unrestricted weighted `\ell^1` ball. Simultaneous recurrence in the finite cadence torus lets a remote logarithmic frequency approach the target phase in all sampled coordinates while the target coefficient changes by order one.

So three losses must be priced separately: **fiber aliasing**, **loss of joint coupling when several marginals are recorded separately**, and **finite-horizon conditioning after exact separation**. More cadences repair none of these automatically. A useful acquisition theorem needs a source restriction, a genuinely mixed/joint observable, nonregular or growing acquisition geometry, or an explicit horizon/precision law tied to the source breadth being recovered.

**Boundary.** The result is for finitely many complete regular lattices on the unrestricted weighted `\ell^1` ordinary-Dirichlet frequency class. Narrow multiplicative/Euler categories, positivity, sparsity, growing cadence families, or joint nonlinear measurements can change both the exact kernel and the stability problem.