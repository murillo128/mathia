# PC-010 — abstract refinement dynamics is the Bost–Connes cyclotomic tower

**Status:** `DECISIVE-NEGATIVE` for the branch that keeps only vertex birth levels and refinement/power maps.

## Claim

Let

\[
\mu_n=\{z\in S^1:z^n=1\},
\qquad
\mu_n^*=\{z\in S^1:\operatorname{ord}(z)=n\}.
\]

The original prime-circle construction regards \(\mu_n\) as the vertices of the regular \(n\)-gon and \(\mu_n^*\) as the vertices that are born for the first time at level \(n\).

If we forget the Euclidean embedding data (chords, crossing positions, off-circle harmonic field, etc.) and retain only

1. the vertices,
2. their birth level,
3. the inclusions induced by divisibility, and
4. the power/refinement maps \(z\mapsto z^k\),

then no new dynamical object remains: this is exactly the classical cyclotomic tower underlying the Bost–Connes endomotive.

## Exact reduction

The union of all polygon vertices is

\[
\mu_\infty:=\bigcup_{n\ge1}\mu_n.
\]

Via

\[
\frac an\pmod 1\longmapsto e^{2\pi i a/n},
\]

we have the canonical group identification

\[
\boxed{\mu_\infty\simeq \mathbb Q/\mathbb Z.}
\]

Moreover, the birth label is not extra information. For every root of unity \(\zeta\),

\[
\boxed{b(\zeta)=\min\{n:\zeta\in\mu_n\}=\operatorname{ord}(\zeta).}
\]

Thus the decorated set \((\zeta,b(\zeta))\) is already determined by the abstract group \(\mathbb Q/\mathbb Z\).

For \(m\mid n\),

\[
\mu_m\subset \mu_n,
\]

and the natural maps between levels are powers

\[
\sigma_k:\zeta\mapsto\zeta^k.
\]

These are precisely the semigroup maps used in the Bost–Connes cyclotomic system. Algebraically the standard arithmetic object is the semigroup crossed product

\[
\mathbb Q[\mathbb Q/\mathbb Z]\rtimes\mathbb N,
\]

and analytically one obtains the corresponding \(C^*\)-dynamical system / endomotive.

Therefore any construction that depends only on the abstract birth-labelled vertices and the maps \(z\mapsto z^k\) factors through already-developed Bost–Connes data.

## Consequence for the current research program

The branch

\[
\boxed{
\text{birth-labelled vertices}
\to
\text{refinement semigroup}
\to
\text{spectrum / partition function / RH}
}
\]

cannot be counted as a novel mechanism unless it uses additional geometric structure that is absent from the abstract cyclotomic tower.

This is especially important because the Bost–Connes system already has \(\zeta(\beta)\) as its partition function and has been extensively developed in relation to cyclotomy, endomotives, noncommutative geometry, and spectral realizations of zeta zeros. Re-deriving those structures from the polygon levels would be a restatement, not new mathematics.

## What the abstract reduction destroys

The radial inversion used by the original interior/exterior geometry is

\[
I(z)=\frac1{\bar z}.
\]

On the unit circle,

\[
I(\zeta)=\zeta.
\]

Hence the inside/outside duality is **invisible on the boundary vertex set itself**. It only becomes nontrivial once one retains off-boundary data such as the harmonic potentials \(U_n(z)=\log|\Phi_n(z)|\), Euclidean chords, crossing locations, or another embedded geometric observable.

This yields a useful research gate:

\[
\boxed{
\text{a genuinely new prime-circle theory must use geometry not recoverable from }
(\mathbb Q/\mathbb Z,\mathbb N).
}
\]

In particular, the promising information is now the embedded geometry between levels, not the abstract refinement tower.

## Literature / novelty check

The identification of all roots of unity with \(\mathbb Q/\mathbb Z\), together with the positive-integer semigroup action and crossed product \(\mathbb Q[\mathbb Q/\mathbb Z]\rtimes\mathbb N\), is the standard Bost–Connes framework. Connes–Consani–Marcolli describe the same cyclotomic tower as a projective system of roots of unity whose maps are the positive-integer power maps, and subsequent endomotive work explicitly identifies its limit with the cyclotomic/Bost–Connes system.

Relevant references include:

- J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Math. (1995).
- A. Connes, C. Consani, M. Marcolli, *Noncommutative geometry and motives: the thermodynamics of endomotives*, Adv. Math. 214 (2007).
- A. Connes, C. Consani, M. Marcolli, *Fun with F1*, J. Number Theory 129 (2009).

No novelty is claimed for this reduction; it is a negative result delimiting where novelty can still live in the original geometric construction.
