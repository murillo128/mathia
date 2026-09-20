# AF-455 — Compact post-processing erases bounded infinite TV marks

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `QUANTITATIVE-FIDELITY`, `OPERATOR-IDEAL`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-454 isolates a genuine escape from bounded finite-dimensional observations: an infinite TV-discrete alphabet can retain a positive uniform margin in a bounded **infinite-dimensional** representation, for example through an orthonormal one-hot code. That escape is fragile under a common next operation. If the downstream post-processing is compact, the required non-precompactness disappears again.

Let `A` be an infinite alphabet, let `X,Y` be Banach spaces, and let

\[
\Phi:A\to X
\]

have bounded image. For one-atom sources define

\[
\kappa_A^{TV}(T\Phi)
=
\frac12\inf_{x\ne y\in A}
\|T\Phi(x)-T\Phi(y)\|_Y.
\tag{1}
\]

Then:

1. **Every compact downstream map kills the uniform TV margin.** If
   \[
   K:X\to Y
   \]
   is compact linear, then
   \[
   \boxed{\kappa_A^{TV}(K\Phi)=0.}
   \tag{2}
   \]
   Thus a bounded infinite-dimensional carrier can evade AF-454 only while its non-precompact output structure survives the later processing chain.

2. **For an orthonormal one-hot carrier, essential norm gives a sharp noncompactness budget.** Let `H` be an infinite-dimensional Hilbert space with orthonormal sequence `(e_n)`, let `Y` be Banach, and let `L\in\mathcal L(H,Y)`. Define
   \[
   \kappa_e^{TV}(L)
   =
   \frac12\inf_{n\ne m}\|L(e_n-e_m)\|_Y.
   \tag{3}
   \]
   With
   \[
   \|L\|_e
   :=
   \inf_{K\in\mathcal K(H,Y)}\|L-K\|
   \tag{4}
   \]
   the essential norm, one has
   \[
   \boxed{
   \kappa_e^{TV}(L)
   \le
   \frac{\|L\|_e}{\sqrt2}.
   }
   \tag{5}
   \]
   Therefore a retained TV margin `c>0` forces
   \[
   \boxed{
   \|L\|_e\ge\sqrt2\,c.
   }
   \tag{6}
   \]
   The constant is sharp: for `Y=H` and `L=aI_H`,
   \[
   \kappa_e^{TV}(aI_H)=\frac{|a|}{\sqrt2},
   \qquad
   \|aI_H\|_e=|a|.
   \tag{7}
   \]

3. **Noncompactness is necessary, not sufficient.** Positive essential norm alone does not guarantee survival of the discriminator. If `P` is the orthogonal projection in `\ell^2` onto the even coordinates, then
   \[
   \|P\|_e=1
   \tag{8}
   \]
   but distinct odd basis vectors are both sent to zero, so
   \[
   \boxed{\kappa_e^{TV}(P)=0.}
   \tag{9}
   \]
   A viable downstream map must therefore spend noncompactness **and** retain separation on the actual source secants.

4. **Compact operator ideals are automatically excluded.** For Hilbert-space targets, every Schatten-class operator `S_p`, `1\le p<\infty`, is compact. In particular finite-rank, trace-class, and Hilbert-Schmidt post-processing all satisfy
   \[
   \boxed{\kappa_e^{TV}(L)=0.}
   \tag{10}
   \]
   on an infinite one-hot alphabet.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{an infinite bounded TV-discrete mark requires non-precompactness not only in its carrier but through every downstream stage; compact smoothing destroys it.}
}
\tag{11}
\]

For the canonical orthonormal carrier, the amount of surviving noncompactness is quantitative: a TV fidelity margin `c` requires at least `\sqrt2 c` of essential norm.

## Derivation

### Compact post-processing restores the AF-454 precompactness obstruction

Because `\Phi(A)` is bounded and `K` is compact, the image

\[
K\Phi(A)
\tag{12}
\]

is relatively norm compact in `Y`, hence totally bounded. AF-454 then applies directly: an infinite family of distinct one-atom TV sources cannot have a positive uniform margin inside a totally bounded observation image. Therefore `(2)` follows.

This is stronger than saying that finite-dimensional post-processing fails. A compact map may have infinite-dimensional range, but its action on bounded sets still produces precompact output. Thus the load-bearing resource exposed by AF-454 is exactly **non-precompactness of the retained source image**, not infinite ambient dimension by itself.

### Compact operators annihilate the orthonormal tail in norm

Let `(e_n)` be orthonormal in `H`. It is weakly null:

\[
e_n\rightharpoonup0.
\tag{13}
\]

If `K:H\to Y` is compact, compactness upgrades weak convergence of this bounded sequence to norm convergence of its image:

\[
\|Ke_n\|_Y\longrightarrow0.
\tag{14}
\]

One direct proof is enough for the present use. The sequence `(Ke_n)` is relatively norm compact, so every subsequence has a norm-convergent subsubsequence. Bounded linearity gives weak convergence `Ke_n\rightharpoonup0`; hence every norm-convergent subsubsequence must converge to `0`. Relative compactness then forces the whole sequence to converge to `0` in norm.

### Essential norm controls the best possible one-hot margin

Fix an arbitrary compact `K:H\to Y`. Pair consecutive orthonormal vectors. From `(14)`,

\[
\|Ke_{2j}\|+\|Ke_{2j+1}\|\longrightarrow0.
\tag{15}
\]

For each `j`,

\[
\begin{aligned}
\|L(e_{2j}-e_{2j+1})\|
&\le
\|(L-K)(e_{2j}-e_{2j+1})\|
 +\|K(e_{2j}-e_{2j+1})\|\\
&\le
\sqrt2\,\|L-K\|
 +\|Ke_{2j}\|+\|Ke_{2j+1}\|.
\end{aligned}
\tag{16}
\]

Taking `j\to\infty` gives

\[
\inf_{n\ne m}\|L(e_n-e_m)\|
\le
\sqrt2\,\|L-K\|.
\tag{17}
\]

After division by the Dirac TV distance `2`,

\[
\kappa_e^{TV}(L)
\le
\frac{\|L-K\|}{\sqrt2}.
\tag{18}
\]

Since `K` was arbitrary compact, taking the infimum proves `(5)`. Rearrangement gives `(6)`.

The inequality has a useful interpretation. The essential norm is not merely a categorical indicator that `L` is noncompact; it is a quantitative lower resource that any uniformly separating one-hot discriminator must spend.

### Sharpness at the identity

For `L=aI_H`, orthonormality gives

\[
\|a(e_n-e_m)\|=|a|\sqrt2
\qquad(n\ne m),
\tag{19}
\]

so

\[
\kappa_e^{TV}(aI_H)=\frac{|a|}{\sqrt2}.
\tag{20}
\]

To compute the essential norm, let `K` be compact. By `(14)`, `Ke_n\to0`, hence

\[
\|(aI_H-K)e_n\|\longrightarrow|a|.
\tag{21}
\]

Therefore `\|aI_H-K\|\ge|a|` for every compact `K`. Choosing `K=0` gives the reverse inequality, so

\[
\|aI_H\|_e=|a|.
\tag{22}
\]

Equations `(20)`--`(22)` attain equality in `(5)`, proving sharpness of the constant.

### Positive essential norm does not encode the relevant secants

Let `P:\ell^2\to\ell^2` be projection onto

\[
\overline{\operatorname{span}}\{e_2,e_4,e_6,\ldots\}.
\tag{23}
\]

For every odd `n`, `Pe_n=0`, so any two distinct odd labels collide and `(9)` follows immediately.

On the even subspace, `P` is the identity. For every compact `K`, the even orthonormal sequence satisfies `Ke_{2j}\to0`, so

\[
\|(P-K)e_{2j}\|
\longrightarrow1.
\tag{24}
\]

Thus `\|P-K\|\ge1`, while `K=0` gives `\|P\|=1`; hence `(8)`.

This control separates two resources that must not be conflated:

\[
\boxed{
\text{noncompactness budget}
\quad\neq\quad
\text{source-relative fidelity}.
}
\tag{25}
\]

The essential norm can certify that an operator has not collapsed into the compact ideal, but it cannot by itself certify that the particular arithmetic or label secants avoid its kernel.

## Arithmetic specialization: prime one-hot marks

Let `\mathbb P` be the rational primes and let

\[
H=\ell^2(\mathbb P),
\qquad
p\mapsto e_p
\tag{26}
\]

be the bounded one-hot prime carrier. Distinct prime Dirac sources satisfy TV distance `2`, while

\[
\|e_p-e_q\|_2=\sqrt2
\qquad(p\ne q).
\tag{27}
\]

Hence the raw carrier has

\[
\kappa_{\mathbb P}^{TV}(I_H)=\frac1{\sqrt2}.
\tag{28}
\]

This realizes exactly the infinite-dimensional escape left open by AF-454: bounded amplitude, infinite alphabet, and a positive uniform TV margin.

Now let `L:H\to Y` be a bounded linear downstream operation. If `L` is compact, the prime margin vanishes. More generally, if the resulting prime observation has margin at least `c>0`, `(6)` forces

\[
\boxed{\|L\|_e\ge\sqrt2 c.}
\tag{29}
\]

Thus a compact smoothing, finite-rank projection, Hilbert-Schmidt kernel, trace-class readout, or other compact spectral post-processing cannot carry a uniformly TV-stable infinite prime label through this one-hot route. The obstruction arises before any subtle property of the primes: the operator category has already destroyed the non-precompact mark required by the source geometry.

This does **not** say that compact operators cannot retain useful arithmetic observables in weaker metrics, on finite prime windows, or for source classes whose normalized secants are precompact. It says only that they cannot preserve a fixed positive TV lower gain on an infinite bounded discrete carrier.

## Relationship to AF-041, AF-075, AF-107, and AF-454

AF-041 shows that stable composition depends on the relative geometry between the surviving upstream range and the downstream kernel. AF-455 identifies a different infinite-family failure mode: even without one fixed killed direction, a compact downstream stage sends a bounded infinite label family into a precompact set, forcing pairwise margins to approach zero.

AF-075 characterizes precompactness through vanishing Kolmogorov widths. Applied to `(12)`, it gives an equivalent approximation-theoretic reading: compact post-processing forces the retained infinite label family to become uniformly approximable by finite-dimensional subspaces, and the TV packing margin must then collapse.

AF-107 studies the converse categorical question of when families of compact approximants assemble to a compact global operator. AF-455 uses the resulting compact category as an **obstruction** rather than a destination: if the final stage is genuinely compact, it is too compressive to preserve an infinite bounded TV-discrete mark.

AF-454 is the immediate source of the present result. It showed that the one-hot escape works only because the bounded orthonormal image is non-precompact. AF-455 closes the next loophole by showing that this non-precompactness must survive downstream, and quantifies the required remainder through the essential norm.

## Prior art and novelty audit

All operator-theoretic ingredients are classical. **No theorem-level novelty is claimed.**

- J. W. Calkin, **“Two-Sided Ideals and Congruences in the Ring of Bounded Operators in Hilbert Space,”** *Annals of Mathematics* 42(4) (1941), 839–873, DOI `10.2307/1968771`. Role: foundational operator-ideal/quotient framework behind measuring an operator modulo compact operators.
- John B. Conway, ***A Course in Functional Analysis***, Graduate Texts in Mathematics 96, Springer. Role: standard functional-analysis reference for compact operators, weak versus norm convergence under compact maps, compact-operator ideals, and quotient/operator-norm structure.
- Robert Schatten, ***Norm Ideals of Completely Continuous Operators***, Ergebnisse der Mathematik und ihrer Grenzgebiete, Springer (1960). Role: classical source for Schatten norm ideals; finite-`p` Schatten classes lie inside the compact operators.
- AF-107 already audited the neighboring classical collectively compact approximation literature of Anselone and Palmer. That literature concerns when compactness survives an approximation/assembly process; the present result asks the complementary fidelity question of what compactness necessarily destroys on an infinite uniformly discrete bounded source image.

A targeted prior-art check also found modern operator-theory literature using the same standard definition

\[
\|L\|_e=\operatorname{dist}(L,\mathcal K)
\]

and the standard weakly-null-sequence test to obtain essential-norm lower bounds. The inequality `(5)` is an elementary specialization of those classical mechanisms to the AF one-hot TV carrier, not a new essential-norm theorem.

The durable Arithmetic Fidelity contribution is the resource statement created by combining those classical facts with AF-454's source geometry: **infinite TV-discrete identity can live in a bounded infinite-dimensional representation, but only in the noncompact part of the downstream operator.** For the orthonormal carrier that requirement is quantitatively sharp via `(5)`--`(7)`.

## Boundary and falsification audit

- **Boundedness of the upstream carrier is load-bearing in `(2)`.** Compact operators control bounded sets. An unbounded label can evade this particular precompactness argument, just as AF-454 already allows unbounded finite-dimensional marks.
- **Infinite ambient dimension is not enough.** A compact operator may have infinite-dimensional range, yet its image of the bounded carrier is precompact and the TV margin still vanishes.
- **Noncompactness is not enough.** The even-coordinate projection `(23)` has maximal essential norm at its scale but destroys infinitely many label distinctions. Source-relative secant separation remains necessary.
- **Essential norm is only an upper controller for this fidelity modulus.** Equation `(5)` does not provide a converse lower bound. Additional transversality or restricted-minimum-modulus information would be needed for sufficiency.
- **The theorem is metric-specific.** Replacing TV with a weaker source metric can change the required packing geometry. AF-453 already exhibits `W_1` as a matched topology where continuous atom motion can remain well conditioned.
- **Finite windows are different.** Every finite alphabet has a positive minimum separation whenever its observed points are distinct. The result concerns a uniform margin over an infinite family.
- **Arithmetic specificity is not created by noncompactness.** A noncompact carrier can preserve labels while remaining completely generic. A later RH-facing application must still show why the surviving noncompact directions encode rational-prime structure rather than an arbitrary enumeration.

The next useful question is therefore narrower than “can infinite dimension rescue TV fidelity?” It can. The remaining issue is to identify natural downstream operator classes that are noncompact enough to meet `(6)` while also remaining source-relative enough to separate the relevant arithmetic secants rather than merely retaining generic infinite-dimensional capacity.