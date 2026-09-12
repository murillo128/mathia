# AF-281 — Joint mixed cadences have common-resonance fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `JOINT-SAMPLING`, `COUPLING`, `ALIASING`, `STABILITY-OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-280 shows that merely concatenating finitely many complete regular vertical lattices does not let individually aliased cadences repair one another on the unrestricted weighted `ell^1` Dirichlet coefficient class. The reason is structural: separate lattice streams retain only separate phase marginals and can annihilate a mixed interaction.

There is a sharp contrasting result if the acquisition keeps **mixed cadence moments** rather than the separate marginals.

Let

\[
F(s)=\sum_{n\ge1} a_n e^{-\lambda_n s},
\qquad
0\le \lambda_1<\lambda_2<\cdots,
\]

and fix `c` with

\[
\sum_{n\ge1}|a_n|e^{-c\lambda_n}<\infty.
\]

For cadences `h_1,\ldots,h_J>0`, retain every mixed sample

\[
\mathcal M_{\mathbf h}(F)
=
\Bigl(F\bigl(c+i(k_1h_1+\cdots+k_Jh_J)\bigr)\Bigr)_{k\in\mathbb Z^J}.
\]

Define the joint phase point

\[
z_n=
\bigl(e^{-ih_1\lambda_n},\ldots,e^{-ih_J\lambda_n}\bigr)
\in\mathbb T^J.
\]

Then the complete mixed channel remembers exactly the coefficient measure after pushforward through `lambda_n -> z_n`:

\[
\boxed{
\mathcal M_{\mathbf h}(F)=\mathcal M_{\mathbf h}(G)
\iff
\sum_n a_ne^{-c\lambda_n}\delta_{z_n}
=
\sum_n a'_ne^{-c\lambda_n}\delta_{z_n}.
}
\]

Consequently, for a common declared frequency system, exact coefficient fidelity holds iff the **joint phase map** `n -> z_n` is injective.

For ordinary Dirichlet series, `lambda_n=log n`. With

\[
R_h=
\{r\in\mathbb Q_{>0}: h\log r\in2\pi\mathbb Z\},
\]

one obtains the exact criterion

\[
\boxed{
\mathcal M_{\mathbf h}\text{ is coefficient-faithful}
\iff
\bigcap_{j=1}^J R_{h_j}=\{1\}.
}
\]

This is strictly weaker than AF-280's criterion for the **separate** lattice channel, which requires at least one individual `R_{h_j}` to be trivial. Thus coupling can genuinely repair exact aliasing.

However, the repair has a sharp acquisition cost. Let

\[
H=\sum_{j=1}^J\mathbb Z h_j\subset\mathbb R.
\]

A finitely generated additive subgroup of the real line is either one discrete lattice `d\mathbb Z` or is dense in `\mathbb R`. In the discrete case, `\mathcal M_{\mathbf h}` is only the single finer lattice channel at spacing `d`. In the dense case, the mixed sample times themselves are dense.

Therefore a finite mixed-cadence family creates no third exact-acquisition regime:

- commensurable cadences reduce to one finer regular lattice;
- incommensurable cadences produce a dense time subgroup.

In particular, if **every individual cadence is resonant**, a strict repair over AF-280 is possible only in the dense-subgroup case. Joint coupling restores exact fidelity by paying arbitrarily fine mixed timing / unbounded integer-combination complexity, not by extracting the lost interaction from finitely many marginal streams.

Finally, this exact infinite-channel repair is not uniformly finite-budget. For every target ordinary coefficient `N`, every finite mixed-index box

\[
|k_j|\le K_j,
\]

and every `epsilon>0`, there are two finite-support Dirichlet series at fixed weighted `ell^1` distance, with weighted coefficient at `N` differing by one, whose mixed samples differ by less than `epsilon` throughout that box. Exact joint fidelity therefore still requires a growing mixed-mode budget or additional source structure.

## Joint Fourier measure classification

Write

\[
b_n=a_ne^{-c\lambda_n},
\qquad
\sum_n|b_n|<\infty,
\]

and define the finite complex measure on the `J`-torus

\[
\mu_F=\sum_{n\ge1}b_n\delta_{z_n}.
\]

For `k=(k_1,\ldots,k_J)\in\mathbb Z^J`,

\[
\begin{aligned}
F\bigl(c+i k\cdot h\bigr)
&=\sum_n b_n
   \exp\!\left(-i\lambda_n\sum_j k_jh_j\right)\\
&=\sum_n b_n\prod_j z_{n,j}^{k_j}\\
&=\int_{\mathbb T^J}z^k\,d\mu_F(z).
\end{aligned}
\]

Thus the mixed samples are all Fourier--Stieltjes coefficients of `mu_F`. Characters `z -> z^k`, `k in Z^J`, determine a finite complex Borel measure on the compact abelian group `T^J`, so equality of every mixed sample is exactly equality of the pushed-forward measures.

This also identifies the full kernel. If several source frequencies have the same joint phase point, only the sum of their weighted coefficients survives. If all joint phase points are distinct, each atom mass is individually recovered.

The distinction from AF-280 is exact. Separate lattices know the `J` coordinate pushforwards of `mu_F`; the mixed channel knows the **joint measure**. The alternating four-point interaction in AF-280 is invisible to each marginal but is visible to some mixed character as soon as the joint phase points are distinct.

## Ordinary Dirichlet common-resonance criterion

For `lambda_n=log n`, two source indices collide jointly iff

\[
e^{-ih_j\log n}=e^{-ih_j\log m}
\quad\text{for every }j.
\]

Equivalently,

\[
h_j\log(n/m)\in2\pi\mathbb Z
\quad\text{for every }j,
\]

which says exactly

\[
\frac nm\in\bigcap_j R_{h_j}.
\]

Hence the intersection of the rational resonance groups, not the individual groups, is the exact alias invariant for mixed acquisition.

Take the two cadences from AF-280,

\[
h_1=\frac{2\pi}{\log2},
\qquad
h_2=\frac{2\pi}{\log3}.
\]

Individually they alias every pair `n,2n` and `n,3n`, respectively. Thus neither separate lattice is faithful, and AF-280 constructs a nonzero four-term coefficient interaction invisible to their concatenation.

But

\[
R_{h_1}=2^{\mathbb Z},
\qquad
R_{h_2}=3^{\mathbb Z},
\qquad
R_{h_1}\cap R_{h_2}=\{1\}.
\]

Therefore the mixed samples

\[
F\!\left(c+2\pi i\left(\frac{k_1}{\log2}+\frac{k_2}{\log3}\right)\right)
\]

recover every ordinary Dirichlet coefficient exactly. The interaction lost by both marginals is restored once products of the two phase coordinates are actually observed.

## The discrete-or-dense acquisition dichotomy

Let `H=sum_j Z h_j`. Any nonzero additive subgroup of `R` is either discrete cyclic or dense. For a finitely generated `H`, the discrete case has

\[
H=d\mathbb Z
\]

for a unique `d>0`. Then every mixed sample time is an integer multiple of `d`, and every integer multiple of `d` is represented by an integer combination of the original cadences. Therefore

\[
\mathcal M_{\mathbf h}(F)
\]

contains exactly the same value data as the single lattice

\[
\bigl(F(c+i\ell d)\bigr)_{\ell\in\mathbb Z},
\]

up to duplicate indexing.

If one of the commensurable original cadences `h_j=m_jd` is rationally resonant, then `d` is also resonant: from a nontrivial rational `r` with

\[
m_jd\log r\in2\pi\mathbb Z
\]

one gets the nontrivial rational `r^{m_j}` with

\[
d\log(r^{m_j})\in2\pi\mathbb Z.
\]

So commensurable mixing cannot repair an alias that is already present in every marginal.

If `H` is nondiscrete, it is dense. If two distinct real frequencies `lambda != lambda'` had the same joint phase tuple, then

\[
e^{-it(\lambda-\lambda')}=1
\quad\text{for every }t\in H.
\]

Continuity and density would make the same identity hold for all real `t`, which is impossible unless `lambda=lambda'`. Thus dense mixed cadence acquisition is automatically coefficient-faithful for every declared system of distinct real frequencies, not only for ordinary Dirichlet frequencies.

This explains the apparent gain over AF-280 without magic: separate marginals discard coupling; complete mixed moments either reduce to a finer one-dimensional lattice or supply a dense subgroup of phase times.

## Finite source breadth is recoverable with finite mixed degree

The infinite-source obstruction should not be confused with finite interpolation.

Suppose the declared source is known a priori to use only `M` frequencies and their joint phase points `z_1,...,z_M` are distinct. For each `n` and each `m != n`, choose a coordinate `j(n,m)` on which `z_n` and `z_m` differ, and define

\[
L_n(z)
=
\prod_{m\ne n}
\frac{z_{j(n,m)}-z_{m,j(n,m)}}
     {z_{n,j(n,m)}-z_{m,j(n,m)}}.
\]

Then `L_n(z_m)=delta_{nm}` and `L_n` has total polynomial degree at most `M-1`. Expanding

\[
L_n(z)=\sum_{|k|_1\le M-1}c_{n,k}z^k,
\qquad k\in\mathbb N^J,
\]

gives

\[
b_n
=
\int L_n\,d\mu_F
=
\sum_{|k|_1\le M-1}
 c_{n,k}
 F(c+i k\cdot h).
\]

So on a **truncated known source**, finitely many mixed samples recover all coefficients exactly whenever the joint phase map separates that finite source. The price is a mode degree that grows with source breadth, and the interpolation coefficients can become badly conditioned when joint phase points approach one another.

This is the finite-dimensional version of the resource law: coupling can replace marginal aliasing, but it does not make unbounded source breadth free.

## Fixed mixed-index boxes have no uniform inverse modulus

Fix an ordinary Dirichlet coefficient `N` and finite bounds `K_1,...,K_J`. Put

\[
\alpha_j=\frac{h_j}{2\pi}.
\]

The cyclic orbit of `alpha=(alpha_1,...,alpha_J)` in `T^J` has arbitrarily large returns to the identity. Hence there are unbounded positive integers `q_l` such that

\[
q_l\alpha_j\to0\pmod1
\quad\text{for every }j.
\]

Choose `m_l` nearest to `Ne^{q_l}`. Then

\[
\log(m_l/N)=q_l+o(1),
\]

and consequently

\[
e^{-ih_j\log m_l}
\to
e^{-ih_j\log N}
\quad\text{simultaneously for all }j.
\]

Take the weighted two-point perturbation

\[
\Delta b_N=1,
\qquad
\Delta b_{m_l}=-1.
\]

Its weighted `ell^1` norm is exactly two and its target displacement at `N` is one. For every fixed mixed-index box,

\[
\max_{|k_j|\le K_j}
\left|
 e^{-i(k\cdot h)\log N}
-e^{-i(k\cdot h)\log m_l}
\right|
\to0.
\]

Thus no fixed finite word-length budget has a source-breadth-independent inverse modulus on the unrestricted ordinary-Dirichlet `ell^1` ball, even when the complete mixed channel is exactly faithful.

The resource omitted by an infinite-channel injectivity statement is therefore explicit: one needs growing mixed mode degree / integer-combination complexity, stronger source compactness or separation, or a target metric that does not require resolving these remote near-collisions.

## Prior art and novelty assessment

All structural ingredients are classical, and no general harmonic-analysis or sampling novelty is claimed.

Walter Rudin, *Fourier Analysis on Groups* (Wiley-Interscience, 1962), supplies the standard uniqueness of Fourier--Stieltjes coefficients for finite measures on compact abelian groups and the subgroup/quotient duality underlying the torus formulation.

Ingo Schoolmann, **“On Bohr's theorem for general Dirichlet series,”** *Mathematische Nachrichten* 293(8) (2020), 1591--1612, DOI `10.1002/mana.201800542`, places vertical traces of general Dirichlet series in classical almost-periodic/Bohr-compactification language and explicitly notes the extension of the monomials to characters.

Carl de Boor and Amos Ron, **“The least solution for the polynomial interpolation problem,”** *Mathematische Zeitschrift* 210 (1992), 347--378, and the broader multivariate interpolation literature establish that interpolation on arbitrary finite node sets is classical. The elementary product formula above is used only to expose a concrete finite mixed-mode budget for this particular torus source.

The additive-subgroup dichotomy `H=dZ` or `H` dense in `R` is elementary classical topological-group theory. Likewise, simultaneous recurrence on `T^J` is a standard compact-group/Kronecker phenomenon.

AF-279 already classifies one regular lattice as a one-torus phase pushforward, and AF-280 classifies a finite family of **separate** lattice marginals. The residual result here is their exact joint-acquisition comparison: on the unrestricted Dirichlet coefficient class, retaining all mixed characters changes the alias criterion from “one marginal is already faithful” to “the common resonance intersection is trivial,” while any strict repair of individually resonant marginals necessarily moves into the dense generated-time regime. This is presented as an Arithmetic Fidelity synthesis of classical facts, not as a new theorem of harmonic analysis.

## Boundaries and failure modes

- Absolute convergence on `Re(s)=c` is assumed so `mu_F` has finite total variation.
- The frequency system is declared. The result recovers amplitudes, not unknown frequencies jointly with amplitudes.
- The complete mixed channel uses every `k in Z^J`. A finite box is a different and unstable acquisition geometry on the unrestricted source class.
- Exact finite-degree interpolation assumes the source itself is truncated to the declared finite frequency set. It does not remove an unknown infinite tail.
- Poor separation of the joint phase points can make the finite interpolation formula arbitrarily ill-conditioned even when it is algebraically exact.
- Separate post-processing of marginal lattice streams cannot synthesize mixed moments that were never observed; AF-280's common-kernel interaction remains invisible there.
- A dense mixed time subgroup gives exact character separation but consumes arbitrarily large integer combinations. This finding does not supply a bounded acquisition budget.
- General signed/complex Dirichlet coefficient fidelity does not automatically imply the same statement for a narrower Euler-product, positive, automorphic, or other arithmetic source category.
- No analytic continuation, functional equation, zero-location theorem, or RH consequence follows from this classification.

## Decisive audit test

When multiple regular cadences are proposed as a repair for arithmetic aliasing, first specify whether the acquisition retains only the separate lattice streams or actually measures mixed combinations.

For separate streams, AF-280 applies: individually resonant cadences cannot repair one another on the unrestricted coefficient class.

For mixed acquisition, compute

\[
\bigcap_j R_{h_j}.
\]

A nontrivial intersection is an exact common alias. A trivial intersection gives exact infinite-channel coefficient fidelity, but then price the resource that created it: if the cadences are commensurable, the channel is only one finer lattice; if they are incommensurable, their integer span is dense and finite word-length boxes remain nonuniformly conditioned.

The relevant fidelity resource is therefore not “number of cadences.” It is **which joint characters are actually observed, how large an integer-combination budget is available, and what source breadth the target requires resolving.**

## Consequence for the research line

AF-278--AF-281 now distinguish four different phase-time resources at fixed real depth. Continuous Bohr averaging recovers coefficients by unbounded time averaging. One regular lattice replaces the source by a one-phase pushforward. Several separate lattices keep only several marginals and cannot repair one another when every marginal aliases. Several mixed cadences keep the joint phase law and can repair those aliases, but a strict repair occurs only by entering the dense integer-span regime; finite mixed-mode budgets remain unstable as source breadth escapes.

This sharpens the current line-wide accounting rule: **cadence diversity and coupling are separate resources**. Exact injectivity of the infinite acquisition says little about compression until the integer-combination budget, phase separation, source breadth, and target recovery modulus are all priced together.