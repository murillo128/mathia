# MC-159 — Finite joint prime-commutator scalarizations are support-only or Mertens-complete

**Status:** `EXACT-DERIVED`, `DECISIVE-NEGATIVE`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the canonical number-state representation and the pulled-back prime commutators from `MC-156`–`MC-158`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_n=\varepsilon_{pn},
\qquad
B_p:=S_p^*[D_\mu,S_p],
\]

\[
B_p\varepsilon_n=b_p(n)\varepsilon_n,
\qquad
b_p(n)=\mu(pn)-\mu(n).
\tag{1}
\]

`MC-158` closes arbitrary scalar functional calculus of **one** fixed prime commutator. A natural relational escape is to keep several prime directions at the same state before scalarizing them.

Fix a finite nonempty set of distinct primes `F`, and write

\[
b_F(n):=(b_p(n))_{p\in F}.
\tag{2}
\]

For each subset `D\subseteq F`, define

\[
(v_D)_p=
\begin{cases}
1,&p\in D,\\
2,&p\notin D.
\end{cases}
\tag{3}
\]

Then the exact joint alphabet is

\[
\boxed{
\mathcal A_F=\{0\}\cup\{\pm v_D:D\subseteq F\},
}
\tag{4}
\]

and for squarefree `n`, with

\[
D_F(n):=\{p\in F:p\mid n\},
\]

one has

\[
\boxed{
b_F(n)=-\mu(n)v_{D_F(n)}.}
\tag{5}
\]

Let

\[
H:\mathcal A_F\to\mathbb C
\tag{6}
\]

be arbitrary, and put

\[
h_0:=H(0),
\qquad
u_D:=\frac{H(v_D)+H(-v_D)}2,
\qquad
c_D:=\frac{H(v_D)-H(-v_D)}2.
\tag{7}
\]

For the cumulative joint scalarization

\[
T_{F,H}(x):=\sum_{n\le x}H(b_F(n)),
\tag{8}
\]

there is an exact decomposition

\[
\boxed{T_{F,H}(x)=E_{F,H}(x)+R_{F,H}(x),}
\tag{9}
\]

where `E_{F,H}` depends only on squarefree support and the finite divisibility pattern `D_F(n)`, while `R_{F,H}` contains all orientation information.

More precisely, if

\[
Q_D(x):=\#\{n\le x:\mu(n)^2=1,\ D_F(n)=D\},
\tag{10}
\]

then

\[
\boxed{
E_{F,H}(x)
=h_0\lfloor x\rfloor
+\sum_{D\subseteq F}(\nu_D-h_0)Q_D(x),
}
\tag{11}
\]

and

\[
\boxed{
R_{F,H}(x)
=-\sum_{D\subseteq F}c_D A_D(x),
}
\tag{12}
\]

with

\[
A_D(x):=
\sum_{\substack{n\le x\\ \mu(n)^2=1\\ D_F(n)=D}}\mu(n).
\tag{13}
\]

The support part is unconditionally square-root controlled after its explicit main term. If

\[
\delta:=\frac6{\pi^2},
\]

then, for fixed `F`,

\[
\boxed{
Q_D(x)=\kappa_Dx+O_F(\sqrt x),
\qquad
\kappa_D
=\delta
\prod_{p\in D}\frac1{p+1}
\prod_{p\in F\setminus D}\frac p{p+1}.
}
\tag{14}
\]

Hence

\[
E_{F,H}(x)=\kappa_{F,H}x+O_{F,H}(\sqrt x)
\tag{15}
\]

for an explicit constant `\kappa_{F,H}`.

The orientation residual has a complete dilation description. Let

\[
(D_pf)(x):=f(x/p),
\qquad
D_D:=\prod_{p\in D}D_p,
\qquad
P_D:=\prod_{p\in D}p,
\tag{16}
\]

with `P_\varnothing=1`. Then

\[
\boxed{
A_D
=(-1)^{|D|}D_D
\prod_{p\in F}(1-D_p)^{-1}M,
}
\tag{17}
\]

where each inverse is the finite-at-each-`x` geometric operator

\[
(1-D_p)^{-1}f(x)=\sum_{j\ge0}f(x/p^j).
\tag{18}
\]

Therefore

\[
\boxed{
\left(\prod_{p\in F}(1-D_p)\right)R_{F,H}
=-Q_H(D)M,
}
\tag{19}
\]

with the multilinear dilation polynomial

\[
\boxed{
Q_H(z)
:=\sum_{D\subseteq F}(-1)^{|D|}c_D
\prod_{p\in D}z_p.
}
\tag{20}
\]

This gives a complete finite-joint dichotomy.

1. If every `c_D=0`, equivalently `H(v_D)=H(-v_D)` for every joint nonzero orbit, then `T_{F,H}` is orientation-blind and reduces exactly to the support/divisibility baseline `(11)`, with the unconditional centered bound `(15)`.
2. If some `c_D\ne0`, then `Q_H` is a nonzero polynomial and the full `F`-semigroup scale family of `R_{F,H}` reconstructs the entire Mertens function **exactly** by a finite recursive dilation decoder.

Thus keeping finitely many prime commutators jointly before an arbitrary scalarization still produces no intermediate information class. The scalarization either removes Möbius orientation completely or retains enough orientation to recover `M` across the multiplicative scale semigroup.

This strictly extends the one-prime scalar boundary of `MC-157`–`MC-158`. A surviving Bost–Connes/semigroup mechanism must use genuinely non-scalar or noncommutative relations, an infinite-prime limit with independently justified topology/regularity, state-to-state distribution/order information not reducible to a finite joint alphabet, or another source-forced carrier outside finite multivariate scalar functional calculus.

## 1. The finite joint alphabet separates support pattern from orientation

For one prime, `MC-156` gives

\[
b_p(n)=
\begin{cases}
0,&\mu(n)=0,\\
-2\mu(n),&\mu(n)\ne0\text{ and }p\nmid n,\\
-\mu(n),&\mu(n)\ne0\text{ and }p\mid n.
\end{cases}
\tag{21}
\]

Taking all `p\in F` simultaneously proves `(4)`–`(5)`. Distinct subsets `D` give distinct positive vectors `v_D`, so the only identification in the actual joint spectrum is the expected sign pair `\pm v_D`.

For squarefree `n` with `D_F(n)=D`, equation `(7)` gives

\[
H(b_F(n))
=H(-\mu(n)v_D)
=\nu_D-c_D\mu(n).
\tag{22}
\]

For nonsquarefree `n`, `b_F(n)=0` and the value is `h_0`. Summing these disjoint cases proves `(9)`–`(13)`.

The even/odd split is therefore not merely formal parity on a finite spectrum. Its even half records exactly the squarefree support together with the finite vector of divisibility bits for the primes in `F`; every dependence on the Möbius sign is concentrated in the coefficients `c_D`.

## 2. Exact-pattern support has only the classical square-root counting error

For fixed finite `F`, the density of squarefree integers with exact divisibility pattern `D` is `(14)`. One direct derivation starts from

\[
\mu(n)^2=\sum_{d^2\mid n}\mu(d)
\tag{23}
\]

and imposes the finitely many conditions `p\mid n` or `p\nmid n` by inclusion-exclusion. The tail of the `d`-sum beyond `\sqrt x` vanishes, and replacing floors by their main terms costs `O_F(\sqrt x)`. The resulting Euler factors are

\[
\frac1{p+1}
\quad(p\in D),
\qquad
\frac p{p+1}
\quad(p\in F\setminus D)
\tag{24}
\]

relative to the global squarefree density `\delta`.

Substituting `(14)` into `(11)` proves `(15)`. In particular, for any fixed `\theta>1/2`, the even contribution cannot hide an unknown `x^\theta` arithmetic term. Any power-scale difficulty above the critical half lies in `R_{F,H}`.

This also supplies a strong matched-control interpretation: any sequence with the same squarefree support has the same support baseline, independently of how its signs are arranged on that support.

## 3. Exact divisibility-pattern Möbius sums are a finite-prime dilation transform of `M`

Let

\[
C_F(x):=
\sum_{\substack{n\le x\\ (n,P_F)=1}}\mu(n),
\qquad
P_F:=\prod_{p\in F}p.
\tag{25}
\]

For one prime `p`, splitting the Möbius sum into terms with and without `p` gives the exact identity

\[
M=(1-D_p)C_{\{p\}}.
\tag{26}
\]

Repeating this finite sieve over the commuting prime dilations gives

\[
\boxed{
M=\left(\prod_{p\in F}(1-D_p)\right)C_F,
}
\tag{27}
\]

hence

\[
\boxed{
C_F=\prod_{p\in F}(1-D_p)^{-1}M.
}
\tag{28}
\]

All geometric expansions terminate pointwise because `M(y)=0` for `0\le y<1`.

Now an integer counted by `A_D` has the unique form

\[
n=P_Dm,
\qquad
(m,P_F)=1,
\qquad
\mu(n)=(-1)^{|D|}\mu(m).
\tag{29}
\]

Therefore

\[
A_D(x)=(-1)^{|D|}C_F(x/P_D),
\tag{30}
\]

which proves `(17)`. Substitution into `(12)` gives `(19)`–`(20)`.

No analytic continuation, Perron inversion, zero-free region, or estimate for `M` enters this transform. It is a finite combinatorial consequence of squarefree multiplicativity and exact prime divisibility.

## 4. Every nonzero odd joint scalarization has an exact recursive decoder

Assume some `c_D\ne0`. Put

\[
q_D:=(-1)^{|D|}c_D,
\qquad
G:=-\left(\prod_{p\in F}(1-D_p)\right)R_{F,H}.
\tag{31}
\]

Then `(19)` says

\[
G(x)=\sum_{D\subseteq F}q_DM(x/P_D).
\tag{32}
\]

Choose among the subsets with `q_D\ne0` one `D_0` for which `P_{D_0}` is minimal. Unique factorization makes all subset products `P_D` distinct, so

\[
P_D>P_{D_0}
\qquad
(D\ne D_0,\ q_D\ne0).
\tag{33}
\]

Evaluating `(32)` at `x=P_{D_0}y` yields

\[
G(P_{D_0}y)
=q_{D_0}M(y)
+\sum_{\substack{D\ne D_0\\q_D\ne0}}
q_DM\!\left(y\frac{P_{D_0}}{P_D}\right).
\tag{34}
\]

Hence

\[
\boxed{
M(y)
=
\frac1{q_{D_0}}
\left[
G(P_{D_0}y)
-
\sum_{\substack{D\ne D_0\\q_D\ne0}}
q_DM\!\left(y\frac{P_{D_0}}{P_D}\right)
\right].
}
\tag{35}
\]

Every Mertens value on the right occurs at a strictly smaller argument than `y`. Iterating `(35)` therefore terminates after finitely many levels, because all shrink factors `P_{D_0}/P_D` are strictly below `1` and `M(t)=0` for `t<1`.

Thus the decoder is triangular in multiplicative scale. The full scalarized scale family determines `M` exactly whenever the joint scalarization has any odd component at all.

This exact injectivity statement is stronger than a generic claim that a finite set of observables contains some sign information. It identifies the source of target completeness: the finite divisibility-pattern decomposition is itself triangular under the rational-prime dilation semigroup.

## 5. Exact recoverability does not automatically give a stable RH-scale criterion

The decoder `(35)` is finite at every fixed `y`, but its constants can amplify under repeated recursion. Thus

\[
R_{F,H}(x)=O(x^\theta)
\]

does not automatically imply the same exponent for `M` for every coefficient choice without a quantitative stability condition on the dilation polynomial `Q_H`.

This is the finite-joint analogue of the conditioning boundary already exposed in `MC-158`. The present conclusion is therefore primarily an **information-classification no-go**: finite joint scalar functional calculus cannot be the desired lossy-but-cancellation-preserving intermediate representation. It either deletes orientation or remains exactly invertible from its natural scale family.

Any future claim of an RH-equivalent norm or growth criterion from such a joint scalarization must separately prove that its inverse dilation recursion preserves the `1/2+\varepsilon` exponent rather than merely relying on exact algebraic recovery.

## 6. What this closes and what remains open

The sequence `MC-149`–`MC-159` now gives a sharper two-sided boundary for the canonical semigroup commutator route.

- Raw norm/essential-norm/Schatten summaries are too weak and admit biased controls.
- All-depth magnitude rows and continuous one-state cluster data remain cancellation-blind (`MC-154`–`MC-155`).
- Exact signed state-labelled coefficients of a single prime are already target-complete (`MC-156`).
- Arbitrary one-prime scalar spectral filters are either support-only or carry the Mertens orientation channel (`MC-157`–`MC-158`).
- The present result shows that **finite same-state joint prime access before arbitrary scalarization does not create a new middle category**.

The remaining relational language must therefore evade at least one hypothesis here. Examples include genuinely noncommutative products or twisted commutators whose value is not a scalar function of the commuting diagonal tuple `(B_p)_{p\in F}`; infinite-prime limits with a source-forced topology or regularity that changes the finite triangular decoder; distributions or correlations between different base states/scales that are not collapsed to pointwise joint alphabets; or another arithmetic relation not equivalent to retaining the complete orientation field.

None of those possibilities is established by this finding.

## Prior-art and novelty audit

The Bost–Connes system, the canonical semigroup representation, and the raw commutator framework are established prior art already audited in `MC-138`–`MC-158`. Joint functional calculus for commuting operator tuples is likewise standard operator theory; in the present finite-spectrum diagonal setting it reduces to the elementary pointwise function `H` on the actual joint spectrum `(4)`.

The targeted prior-art search used for this continuation again located the standard Bost–Connes and noncommutative-geometric literature, including Greenfield, Marcolli and Teh, *Twisted Spectral Triples and Quantum Statistical Mechanical Systems* (2014), DOI `10.1134/S2070046614020010`, which explicitly shows that richer twisted structures exist beyond the raw commuting scalarization classified here. It did not locate this exact finite-joint Möbius commutator support/orientation classification or the triangular decoder `(35)`. No novelty inference is drawn from that absence: the derivation is an elementary finite extension of the coefficient identities already persisted in `MC-156`–`MC-158`.

Accordingly the result is recorded as `EXACT-DERIVED` and `NO-NOVELTY-CLAIM`. The literature boundary matters only to prevent the finite scalar no-go from being overextended to twisted or genuinely noncommutative Bost–Connes constructions.

## Boundaries and falsification tests

- **Finite prime set only.** The theorem fixes finite `F`. An infinite-prime completion can change topology, convergence, regularity, and information content and needs its own theorem.
- **Commuting pulled-back tuple only.** Every `B_p` here is diagonal, so `H((B_p)_{p\in F})` is ordinary finite joint functional calculus. Noncommutative expressions involving the shifts `S_p`, alternative representations, twisted commutators, or different Dirac data are outside the claim.
- **Same-state scalarization followed by ordinary prefix aggregation.** Correlations between different base states, distributions of joint rows, state transitions, or additive ordering are not classified unless they reduce to `(8)`.
- **Support baseline is not zero information.** It uses only `\mu^2` and finitely many divisibility bits; its centered square-root estimate is unconditional. Exact subtraction of `(11)` is therefore not an RH assumption.
- **Exact recovery is not a free power estimate.** The recursion `(35)` may be poorly conditioned. Any claimed critical-exponent transfer must audit coefficient amplification separately.
- **No Mertens improvement.** The theorem closes a representation-level candidate class. It does not improve the unconditional bound for `M`, prove a new zero-free region, or supply evidence for RH.
- **Distinct subset products are load-bearing.** The triangular decoder uses unique factorization to order the active dilation monomials by `P_D`. A proposed generalization to a different semigroup with collisions among scale products requires a separate injectivity argument.

## Consequence for the line

Finite same-state joint scalarization is now closed as a candidate intermediate carrier. Adding finitely many prime directions does not interpolate between the support-blind and target-complete endpoints found at one prime: after exact support subtraction, every surviving orientation component is a nonzero finite dilation polynomial in `M`, and unique factorization makes that polynomial recursively invertible over its natural scale semigroup.

The next Bost–Connes/semigroup candidate should therefore be killed immediately if, after pulling back the shifts, it reduces to an arbitrary scalar function of finitely many diagonal prime differences followed by prefix summation. A genuinely new route must change the information architecture rather than enlarge the finite scalar alphabet.