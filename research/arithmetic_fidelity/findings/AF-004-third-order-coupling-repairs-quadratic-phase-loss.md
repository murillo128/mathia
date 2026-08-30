# AF-004 — Third-order coupling can repair quadratic phase loss on finite abelian groups

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`

## Claim

Let `G` be a finite abelian group written additively, let `\widehat G` be its character group, and for a complex signal

\[
f:G\to\mathbb C
\]

define the Fourier transform

\[
\widehat f(\chi)=\sum_{x\in G} f(x)\,\overline{\chi(x)}.
\]

Define the translation action

\[
(\tau_t f)(x)=f(x-t),
\]

the power spectrum

\[
P_f(\chi)=|\widehat f(\chi)|^2,
\]

and the bispectrum

\[
B_f(\chi,\psi)
=\widehat f(\chi)\widehat f(\psi)
\overline{\widehat f(\chi\psi)}.
\]

Then:

1. `P_f` is exactly the Fourier transform of the ordinary autocorrelation
   \[
   A_f(h)=\sum_{x\in G}f(x+h)\overline{f(x)}.
   \]
   Thus ordinary autocorrelation / Fourier-magnitude compression forgets Fourier phase.
2. The power spectrum is not a complete invariant modulo translation, even on a finite cyclic group: distinct non-translate signals can have identical `P_f`.
3. Both `P_f` and `B_f` are translation-invariant.
4. If `f` and `g` have **nonzero Fourier coefficients at every character**, then
   \[
   P_f=P_g,\qquad B_f=B_g
   \]
   holds if and only if `g` is a translate of `f`.

Consequently, in this exact model, a second-order canonical compression has fibers strictly larger than the intended translation symmetry, while adding third-order phase coupling collapses the generic fiber back to exactly one translation orbit. This gives Arithmetic Fidelity a concrete recovery pattern in which **relational coupling between already-retained coordinates restores provenance that their individual magnitudes erase**.

The result is classical bispectral / higher-order-correlation mathematics, not a new theorem. Its value for this line is as a clean model separating a lossy canonical invariant from a stronger invariant that is complete modulo the intended symmetry.

## Derivation

For the autocorrelation statement, take the Fourier transform in the `h` variable:

\[
\begin{aligned}
\widehat A_f(\chi)
&=\sum_{h\in G}\sum_{x\in G}
 f(x+h)\overline{f(x)}\,\overline{\chi(h)}\\
&=\sum_{x,y\in G}
 f(y)\overline{f(x)}\,\overline{\chi(y-x)}\\
&=\left(\sum_y f(y)\overline{\chi(y)}\right)
  \left(\sum_x\overline{f(x)}\chi(x)\right)\\
&=|\widehat f(\chi)|^2.
\end{aligned}
\]

Hence the autocorrelation and the Fourier magnitudes contain the same information.

Translation acts on Fourier coefficients by

\[
\widehat{\tau_t f}(\chi)
=\overline{\chi(t)}\,\widehat f(\chi).
\]

The multiplier has unit modulus, so `P_f` is translation-invariant. In the bispectrum the three translation factors cancel because

\[
\overline{\chi(t)}\,\overline{\psi(t)}\,
\overline{\overline{(\chi\psi)(t)}}=1,
\]

so `B_f` is translation-invariant as well.

To see directly that the power spectrum is not complete, take

\[
G=\mathbb Z/3\mathbb Z
\]

and define two signals through their Fourier coefficients, indexed by `k=0,1,2`, by

\[
\widehat f=(1,1,1),
\qquad
\widehat g=(1,1,i).
\]

The inverse discrete Fourier transform gives legitimate signals on `G`, and

\[
P_f=P_g=(1,1,1).
\]

If `g` were a translate of `f`, the ratio

\[
r_k=\frac{\widehat g(k)}{\widehat f(k)}
\]

would be the character multiplier associated with one translation. Since `r_1=1`, that translation must be trivial on `\mathbb Z/3\mathbb Z`, which would force `r_2=1`; but `r_2=i`. Hence the two signals are not translates despite having identical autocorrelation/power spectrum.

Now assume all Fourier coefficients of `f` and `g` are nonzero and that their power spectra and bispectra agree. Define

\[
r(\chi)=\frac{\widehat g(\chi)}{\widehat f(\chi)}.
\]

Equality of power spectra gives

\[
|r(\chi)|=1
\qquad\text{for every }\chi.
\]

Equality of bispectra gives

\[
r(\chi)r(\psi)\overline{r(\chi\psi)}=1.
\]

Because `|r|=1`, this is equivalent to

\[
r(\chi\psi)=r(\chi)r(\psi).
\]

Thus `r` is a character of the dual group `\widehat G`. Finite Pontryagin duality identifies every such character with evaluation at some `t\in G`; with the present Fourier convention,

\[
r(\chi)=\overline{\chi(t)}
\]

for some `t`. Therefore

\[
\widehat g(\chi)
=\overline{\chi(t)}\widehat f(\chi)
=\widehat{\tau_t f}(\chi)
\]

for every character, and Fourier inversion gives

\[
g=\tau_t f.
\]

The converse was already proved by translation invariance. Hence `(P_f,B_f)` is complete modulo translation on the nonvanishing-Fourier locus.

## Structural interpretation

The power spectrum retains the magnitudes

\[
|\widehat f(\chi)|
\]

but removes the relative phases of distinct Fourier coordinates. Its fiber therefore permits many phase assignments that are not induced by one global translation.

The bispectrum does not simply append another independent scalar to each coordinate. It records the **triadic compatibility law**

\[
\arg B_f(\chi,\psi)
=\arg\widehat f(\chi)+\arg\widehat f(\psi)
-\arg\widehat f(\chi\psi),
\]

whenever the participating coefficients are nonzero. Equality of all those couplings forces the phase ratio between two candidates to obey the group law, turning a collection of independent local phase freedoms into one global character. Pontryagin duality then identifies that residual character with precisely the symmetry that was intended to be forgotten: translation.

This is a stronger Arithmetic Fidelity lesson than the slogan that “phase matters.” The relevant retained datum is a **relation among phases**. A representation can discard each absolute phase while still preserve enough higher-order compatibility to identify the upstream object modulo a controlled symmetry.

## Relation to AF-001 through AF-003

AF-001 says recoverability is determined by whether a discriminator is constant on the compression fibers. Here the compression `f\mapsto P_f` has fibers larger than translation orbits, so any discriminator that separates some of those extra phase choices is lost.

AF-002 says selecting from a fixed coordinate library is a classical discernibility problem. The bispectral rescue is different: its usefulness comes from coupled products of Fourier coordinates rather than from choosing a subset of independent predeclared attributes.

AF-003 says a symmetry-constrained observable class should be judged by its maximal quotient. The present example shows that **not all translation-invariant observable classes induce the same quotient**. Quadratic translation invariants are incomplete, while an appropriate third-order invariant family is complete on a nondegenerate locus. Requiring invariance under a symmetry therefore does not by itself determine how much additional structure is lost; the algebra/order of the invariant family matters.

## Prior art and novelty assessment

The identity between autocorrelation and Fourier magnitude is classical Fourier analysis and is the standard entrance to the phase-retrieval problem. Modern phase-retrieval surveys emphasize that one-dimensional Fourier magnitude is generally non-unique without additional information.

Bartelt, Lohmann, and Wirnitzer (1984) developed explicit phase and amplitude recovery from bispectra. Yellott and Iverson (1992) studied when higher-order autocorrelation functions uniquely determine an image and also exhibited important failures outside favorable finite-support settings. Kakarala and Iverson (1993) analyzed the periodic case and showed that triple correlation is not universally complete there; their broader moment-spectrum results make clear that the required correlation order depends on spectral structure. Kakarala's later group-theoretic treatment develops bispectral completeness for compact-group settings under nondegeneracy hypotheses.

The finite-abelian proof above is therefore a simple specialization/rederivation of classical bispectral completeness, not a novelty claim. The Mathia-specific contribution is the **fidelity interpretation**: it provides a worked example where the correct response to a lossy canonical compression is not to reattach the original phase as a mark, but to add an intrinsic higher-order relational observable whose consistency equations reduce the excess fiber exactly to the intended symmetry orbit.

## Boundaries and failure modes

- The completeness theorem assumes every Fourier coefficient is nonzero. This is a genuine structural condition, not a technical decoration.
- When Fourier coefficients vanish, bispectral equations constrain phase ratios only on triples `\chi,\psi,\chi\psi` lying inside the nonzero Fourier support. Gaps can disconnect the phase-coupling constraints, and triple correlation need not remain complete.
- Equality of power spectrum plus bispectrum is only one recovery design. Other additional measurements, masks, priors, support constraints, or non-correlation observables may also resolve phase retrieval.
- The theorem establishes completeness **modulo translation**, not absolute recovery. Translation is deliberately invisible to both invariants.
- No universal minimality of third order is claimed. The result is minimal only in the informal sense of comparing the ordinary second-order correlation with one natural next-order correlation family; a different admissible measurement class can change the problem.
- The argument is finite, exact, deterministic, and abelian. Compact nonabelian groups require matrix-valued Fourier components and stronger representation-theoretic hypotheses.
- Nothing here identifies an arithmetic discriminator or proves that bispectral data are the right lift for any RH construction.

## Decisive audit test for higher-order recovery claims

When a compression loses coordinatewise phase, orientation, sign, or provenance and a proposed rescue uses higher-order relations:

1. identify the residual freedom inside a fiber of the lower-order compression;
2. write the exact compatibility equations imposed by the higher-order observable;
3. solve the stabilizer of those equations rather than merely observing improved discrimination numerically;
4. compare that stabilizer with the symmetry that the representation was intentionally allowed to forget;
5. inspect degeneracy loci where coefficients vanish or couplings disconnect.

The rescue is structurally faithful only when the remaining fiber is no larger than the intended symmetry class.

## Consequence for the line

Add **correlation/order hierarchy** to the line's model library. A lower-order invariant can be canonical yet incomplete, while a higher-order relational invariant can preserve exactly the missing compatibility without restoring forbidden absolute labels.

The next useful abstraction is to study the coupling structure generated by an admissible family: which coordinates become linked by its relations, what residual gauge group survives those links, and how zeros or missing interactions split that coupling structure into independently movable components. That question is broader than Fourier bispectra and can be tested in Gram/tensor invariants, moment hierarchies, spectral multiplicative relations, and eventually arithmetic compression chains.