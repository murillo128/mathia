# AF-040 — Pairwise stability does not imply multichannel stability

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `H` be a real or complex Hilbert space, let

\[
M_1,\ldots,M_m\subset H
\]

be closed subspaces, and let `P_i` be the orthogonal projection onto `M_i`. Put

\[
W=\overline{M_1+\cdots+M_m}.
\]

Define the analysis, synthesis, and fusion operators

\[
\mathcal A:W\to\bigoplus_{i=1}^m M_i,
\qquad
\mathcal A h=(P_1h,\ldots,P_mh),
\]

\[
B:\bigoplus_{i=1}^m M_i\to W,
\qquad
B(x_1,\ldots,x_m)=\sum_{i=1}^m x_i,
\]

and

\[
S=\mathcal A^*\mathcal A=BB^*=\sum_{i=1}^m P_i
\quad\text{on }W.
\]

Then:

1. **Exact fidelity is automatic on the generated support.**
   \[
   \boxed{\ker(\mathcal A|_W)=\{0\}.}
   \]
   Equivalently, the support projection of `S` is `P_W`.

2. **Stable fidelity is exactly a collective closed-sum condition.** If
   \[
   \alpha
   =
   \inf_{\substack{h\in W\\\|h\|=1}}
   \sum_{i=1}^m\|P_i h\|^2,
   \]
   then
   \[
   \boxed{
   \alpha>0
   \iff
   \mathcal A|_W\text{ is bounded below}
   \iff
   M_1+\cdots+M_m\text{ is closed}.
   }
   \]
   In the stable case `S|_W` is boundedly invertible and
   \[
   h=(S|_W)^{-1}\sum_{i=1}^m P_i h.
   \]

3. **Pairwise stability is not enough.** There exist three closed subspaces `M_1,M_2,M_3` such that every pairwise sum `M_i+M_j` is closed, with all pairwise Friedrichs cosines bounded strictly below `1`, while
   \[
   M_1+M_2+M_3
   \]
   is dense and nonclosed. The complete three-channel observation remains exactly injective on `H`, but its optimal lower fusion-frame bound is zero.

4. **The failure can occur despite a uniform fixed pairwise gap.** In the explicit construction below,
   \[
   c(M_1,M_2)=0,
   \qquad
   c(M_1,M_3)=c(M_2,M_3)=\frac1{\sqrt2},
   \]
   so every pair has the same positive stability margin independently of scale. Nevertheless there are unit vectors `h_k` for which
   \[
   \sum_{i=1}^3\|P_i h_k\|^2
   =\frac1{2k^2+1}\longrightarrow0.
   \]

Thus the reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{multichannel stability is collective geometry; pairwise separation does not control the full fusion operator.}
}
\]

A compression built from several individually or pairwise well-conditioned retained channels therefore needs a global lower-frame/closed-sum audit. Pairwise collision tests alone cannot certify stable survival of the jointly retained discriminator.

## Derivation

### Exact support fidelity

For `h\in H`,

\[
\mathcal Ah=0
\iff
h\in\bigcap_{i=1}^m M_i^\perp
=\left(M_1+\cdots+M_m\right)^\perp
=W^\perp.
\]

Hence restricting to `W` gives `\ker(\mathcal A|_W)=\{0\}`. Also

\[
\langle Sh,h\rangle
=\sum_{i=1}^m\|P_i h\|^2,
\]

so `\ker S=W^\perp` on `H` and the support projection of `S` is `P_W`. This is the finite-channel specialization of the support mechanism already isolated in AF-038.

### Stable fidelity is closedness of the collective algebraic sum

By definition,

\[
\alpha>0
\iff
\|\mathcal Ah\|^2\ge\alpha\|h\|^2
\quad(h\in W),
\]

so `\alpha>0` is exactly bounded-below analysis on the generated support.

Because `\mathcal A|_W` is injective, it is bounded below exactly when its range is closed. The Hilbert-space closed-range theorem gives

\[
\operatorname{Ran}\mathcal A\text{ closed}
\iff
\operatorname{Ran}\mathcal A^*\text{ closed}.
\]

But `\mathcal A^*=B` and

\[
\operatorname{Ran}B=M_1+\cdots+M_m.
\]

Therefore

\[
\alpha>0
\iff
M_1+\cdots+M_m\text{ is closed}.
\]

Since its closure is `W`, closedness means exactly that the algebraic sum already equals the generated support. In that case `S=\mathcal A^*\mathcal A` satisfies

\[
S\ge\alpha I_W
\]

and the reconstruction formula follows. If the total sum is nonclosed, exact injectivity survives but the inverse from retained channel data to `W` is unbounded.

This identifies the missing global condition left open by AF-038. AF-039 gives the sharp two-channel scalar `1-c(M,N)`; for more channels the invariant is the bottom of the actual collective fusion spectrum, equivalently closedness of the total synthesis range.

## Explicit three-channel control

Let

\[
H_0=\ell^2(\mathbb N),
\qquad
H=H_0\oplus H_0\oplus H_0,
\]

and define the bounded injective diagonal operator

\[
De_k=\frac1k e_k.
\]

Its range is dense and nonclosed. Define

\[
M_1=H_0\oplus\{0\}\oplus\{0\},
\]

\[
M_2=\{0\}\oplus H_0\oplus\{0\},
\]

and

\[
M_3=\{(x,x,Dx):x\in H_0\}.
\]

Writing

\[
Rx=(x,x,Dx),
\]

we have

\[
\|Rx\|^2=2\|x\|^2+\|Dx\|^2\ge2\|x\|^2,
\]

so `R` is bounded below and `M_3=\operatorname{Ran}R` is closed.

### Every pair is stably separated

Clearly

\[
M_1+M_2=H_0\oplus H_0\oplus\{0\},
\]

which is closed. Also

\[
M_1+M_3
=\{(a,x,Dx):a,x\in H_0\}
=H_0\oplus\operatorname{graph}(D),
\]

up to the evident coordinate grouping, hence it is closed because `D` is bounded and its graph is closed. Similarly `M_2+M_3` is closed.

The pairwise intersections are zero. For `M_1` and `M_3`,

\[
\sup_{\substack{u,x\ne0}}
\frac{|\langle (u,0,0),(x,x,Dx)\rangle|}
{\|u\|\sqrt{2\|x\|^2+\|Dx\|^2}}
=
\sup_{x\ne0}
\frac{\|x\|}{\sqrt{2\|x\|^2+\|Dx\|^2}}.
\]

Because `D` is injective but not bounded below, the last supremum is

\[
\frac1{\sqrt2}.
\]

Thus

\[
c(M_1,M_3)=\frac1{\sqrt2},
\qquad
c(M_2,M_3)=\frac1{\sqrt2},
\qquad
c(M_1,M_2)=0.
\]

By AF-039, each pair has a positive lower stability bound; for the two nonorthogonal pairs the sharp reduced bound is `1-1/\sqrt2`.

### The triple is exact but unstable

The total algebraic sum is

\[
M_1+M_2+M_3
=H_0\oplus H_0\oplus\operatorname{Ran}D.
\]

Since `\operatorname{Ran}D` is dense and nonclosed,

\[
\overline{M_1+M_2+M_3}=H
\]

but the algebraic sum is not closed. The theorem above therefore already implies exact three-channel fidelity with zero stable lower bound.

There is also an explicit instability sequence. Let

\[
h_k=(0,0,e_k).
\]

Then `\|h_k\|=1` and

\[
P_1h_k=P_2h_k=0.
\]

For the third projection, since

\[
R^*R=2I+D^2
\]

and

\[
R^*h_k=De_k=\frac1k e_k,
\]

the orthogonal projector onto `M_3=\operatorname{Ran}R` is

\[
P_3=R(R^*R)^{-1}R^*,
\]

and hence

\[
\begin{aligned}
\|P_3h_k\|^2
&=\langle R^*h_k,(R^*R)^{-1}R^*h_k\rangle\\
&=\frac{k^{-2}}{2+k^{-2}}\\
&=\frac1{2k^2+1}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_{i=1}^3\|P_i h_k\|^2
=\frac1{2k^2+1}\to0.
}
\]

No nonzero vector is annihilated by all three projections because the three subspaces generate a dense subspace of `H`. This is therefore not an exact collision hidden inside one bad pair: it is a purely collective loss of conditioning.

## Finite-scale consequence

Let `H_0^{(n)}=\operatorname{span}\{e_1,\ldots,e_n\}` and truncate all three subspaces accordingly. Every finite-dimensional three-channel system is stably recoverable because exact injectivity on its generated support implies a positive smallest singular value. Yet the test vector `h_n=(0,0,e_n)` gives

\[
\alpha_n
\le
\frac1{2n^2+1}\longrightarrow0.
\]

The pairwise Friedrichs cosines of the infinite system remain fixed at `0` or `1/\sqrt2`; in particular, no pairwise angle is drifting toward the bad boundary `1`. Thus even a uniform pairwise stability audit does not prevent the collective multichannel constant from collapsing in an asymptotic limit.

This strengthens the finite-stage warning in AF-039: one cannot rescue a global limit argument by checking every pair separately.

## Prior art and novelty assessment

The operator-theoretic ingredients are classical, and no novelty is claimed for fusion frames, closed-range theorems, generalized Friedrichs angles, or criteria for closed sums of finitely many subspaces.

- Peter G. Casazza and Gitta Kutyniok, **“Frames of subspaces,”** *Contemporary Mathematics* 345 (2004), 87–113, DOI `10.1090/conm/345/06242`. Role: foundational frame-of-subspaces language for analysis, synthesis, frame operators, and stable reconstruction from collections of subspaces.
- Peter G. Casazza, Gitta Kutyniok, and Shidong Li, **“Fusion frames and distributed processing,”** *Applied and Computational Harmonic Analysis* 25(1) (2008), 114–132, DOI `10.1016/j.acha.2007.10.001`. Role: standard fusion-frame framework and reconstruction from distributed subspace data.
- Constantin Badea, Sophie Grivaux, and Vladimir Müller, **“A generalization of the Friedrichs angle and the method of alternating projections,”** *Comptes Rendus Mathématique* 348 (2010), 53–56, DOI `10.1016/j.crma.2009.11.018`. Role: explicit extension of Friedrichs-angle geometry from two subspaces to arbitrary finite families.
- Ivan Feshchenko, **“On the closedness of the sum of n subspaces of a Hilbert space,”** *Ukrainian Mathematical Journal* 63(10), 1566–1622, DOI `10.1007/s11253-012-0601-9`. Role: direct prior art for necessary and sufficient conditions governing closedness of finite sums of closed Hilbert subspaces.

The present finding does not claim that the general equivalence or the existence of pairwise-closed/nonclosed-total configurations is new. Its Arithmetic Fidelity contribution is the compression audit they force: AF-038's exact fusion support and AF-039's two-channel angle criterion cannot be promoted pairwise to a multichannel guarantee. The explicit diagonal-graph control makes the failure quantitative while keeping every pair uniformly away from the two-channel instability boundary.

## Boundaries and failure modes

- The theorem assumes that the destination actually retains the full projection vectors `(P_i h)_i`, or information exactly equivalent to them. Scalar norms, traces, spectra, moments, or pairwise summaries are further compressions and need separate audits.
- Closedness and the lower bound depend on the Hilbert topology and destination norm. A different norm can change conditioning and must be independently justified.
- Pairwise closedness is neither asserted nor needed for exact support fidelity. It is included only to show that a strong family of local checks still fails to control the global lower spectrum.
- The explicit triple is a structural control, not an arithmetic model. A prime/RH application must identify actual retained channels and prove that their joint observation factors through the proposed destination.
- For more than two channels, no scalar built only from the individual pairwise Friedrichs cosines can certify stability in general, because the example fixes all three pairwise cosines strictly below `1` while the collective lower bound is zero.
- A finite-dimensional truncation is automatically stable once injective, but that fact has no asymptotic force without a uniform collective lower bound.

## Decisive audit test

Whenever a proposed compression claims stable recovery from several retained relational channels:

1. identify the actual Hilbert subspaces or channel ranges visible in the destination;
2. form the complete analysis operator `\mathcal A` and fusion operator `S=\sum_iP_i` rather than only pairwise overlaps;
3. prove a uniform positive lower bound for `S` on the generated support, equivalently prove that the total algebraic synthesis range is closed;
4. under truncation or limiting procedures, track that lower bound uniformly rather than checking injectivity at each finite stage;
5. reject any argument that substitutes uniformly good pairwise angles for the collective lower-spectrum gate without an additional theorem specific to the source class.

For Arithmetic Fidelity, this supplies a reusable no-go gate for multicarrier or multi-observable constructions: local compatibility and pairwise stability do not establish global stable fidelity.