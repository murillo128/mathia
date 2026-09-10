# FD-029 — growing initial-prime ancestry is a lossless Möbius recovery hierarchy

**Status:** `EXACT-DERIVED + CLASSICAL-MOBIUS-FACTORING + SCALE-GROWING-PRIME-ANCESTRY + ROUGH-CORE-PARAMETRIZATION + COMMON-SOURCE-RECOVERY + INFORMATION-BOUNDARY + NEGATIVE/OBSTRUCTION`.

`FD-027` shows that any fixed finite set of exact prime-direction identities can coexist with sparse-horizon GCD-duality saturation. `FD-028` strengthens this to infinitely many prime directions when that infinite set is sufficiently sparse. The live question left by those controls is how much prime ancestry must be visible at the active scale before the residual sign freedom changes qualitatively.

There is a sharp information boundary that must be separated from a genuine coercive estimate. If the enforced prime directions form an **initial segment of the primes**, then their finite-scale effect admits an exact rough-core parametrization; if that initial segment grows without bound on one common source, the hierarchy eventually recovers the Möbius function pointwise. Thus an exact scale-growing prime-prefix condition is not an asymptotic free-source relaxation in the same sense as `FD-027`--`FD-028`.

Fix integers `H>=1` and a real threshold `1<=Y<=H`. Let `a_1,...,a_H` satisfy

\[
a_1=1,
\qquad
a_n=0\quad(n\le H\text{ nonsquarefree}),
\qquad
a_n\in\{-1,+1\}\quad(n\le H\text{ squarefree}),
\tag{1}
\]

and impose the exact prime-prefix ancestry law

\[
\boxed{
a_{pn}=-a_n
\quad\text{for every prime }p\le Y,\ p\nmid n,\ pn\le H.
}
\tag{2}
\]

Let

\[
\mathcal S_Y:=\{q:q\text{ squarefree and every prime divisor of }q\text{ is }\le Y\},
\]

\[
\mathcal R_Y:=\{r:r\text{ squarefree and every prime divisor of }r\text{ is }>Y\},
\tag{3}
\]

with `1` in both conventions where appropriate. Then every squarefree `n<=H` factors uniquely as `n=qr` with `q in S_Y` and `r in R_Y`, and (2) is equivalent to

\[
\boxed{
a_{qr}=\mu(q)b_r,
\qquad b_1=1,
\qquad b_r\in\{-1,+1\}\ (r\in\mathcal R_Y,\ r>1).
}
\tag{4}
\]

The variables `b_r` are the **entire residual freedom**. In particular, if `Y>=H^beta` for a fixed `0<beta<=1`, every free rough core obeys

\[
\boxed{
\omega(r)\le \left\lceil\frac1\beta\right\rceil-1.
}
\tag{5}
\]

At the square-root threshold `Y>=sqrt(H)`, the only free rough cores are single primes `p>Y`. At the stronger linear threshold `Y>=H/2`, every entry of the Farey--Mertens horizon vector except the endpoint is already the physical Mertens entry; the remaining freedom is one-dimensional endpoint doping.

Most importantly, suppose one **common infinite source** satisfies the squarefree support/sign conditions and there are `H_j->infinity`, `Y_j->infinity` for which (2) holds through `(H_j,Y_j)` for every `j`. Then

\[
\boxed{a_n=\mu(n)\quad\text{for every }n>=1.}
\tag{6}
\]

The rate at which `Y_j` tends to infinity is irrelevant. Any fixed integer has only finitely many prime divisors, so eventually all of its prime directions are inside one enforced prefix and its coefficient is forced to the Möbius value.

This does **not** say that using Möbius multiplicativity in an argument is circular or that full multiplicativity proves RH. It says something narrower about the control program: exact prime-by-prime breadth that grows through complete initial prime segments eventually stops being a non-Möbius common-source relaxation. A useful next coercive condition must therefore distinguish a quantitative estimate from mere pointwise source recovery—for example through an aggregate/approximate breadth law, or through a finite-scale theorem that proves a GCD-energy gap before the exact hierarchy exhausts the source.

## 1. Exact factorization of the residual source freedom

Let `n<=H` be squarefree and write

\[
n=qr,
\qquad
q:=\prod_{\substack{p\mid n\\p\le Y}}p,
\qquad
r:=\prod_{\substack{p\mid n\\p>Y}}p.
\tag{7}
\]

Then `q in S_Y`, `r in R_Y`, `(q,r)=1`, and the factorization is unique. Starting from `a_r=b_r`, apply (2) once for every prime divisor of `q`. Every intermediate product is at most `qr=n<=H`, and none of the newly introduced primes divides the previous product. Each step changes the sign, so

\[
a_{qr}=(-1)^{\omega(q)}b_r=\mu(q)b_r,
\tag{8}
\]

which proves the forward implication in (4).

Conversely, choose arbitrary signs `b_r` on the rough squarefree cores and define `a` by (4), with `a_n=0` on nonsquarefree integers. If `p<=Y`, `p\nmid n`, and `pn<=H`, multiplication by `p` adds exactly one prime to the `q` factor while leaving the rough core unchanged. Hence

\[
a_{pn}=\mu(pq)b_r=-\mu(q)b_r=-a_n.
\tag{9}
\]

For nonsquarefree `n` both sides are zero. Thus (4) is an exact parametrization, not merely a necessary condition.

This makes the difference from `FD-028` explicit. There the enforced infinite prime set was chosen sparse enough that an abundant `S`-free squarefree core survived at every planted scale. Here the enforced set contains **every** prime up to `Y`; the free core consists exactly of squarefree integers whose prime factors all lie beyond that moving cutoff.

## 2. Exact cumulative defect decomposition

Define the truncated smooth Möbius sum

\[
M_Y(x):=
\sum_{\substack{q\le x\\q\in\mathcal S_Y}}\mu(q).
\tag{10}
\]

Writing `A(x)=sum_(n<=x) a_n`, equation (4) and unique factorization give, for every `x<=H`,

\[
\boxed{
A(x)=
\sum_{\substack{r\le x\\r\in\mathcal R_Y}}
 b_r\,M_Y\!\left(\left\lfloor\frac xr\right\rfloor\right).
}
\tag{11}
\]

The physical Möbius function has the same decomposition with `b_r=mu(r)`:

\[
M(x)=
\sum_{\substack{r\le x\\r\in\mathcal R_Y}}
 \mu(r)\,M_Y\!\left(\left\lfloor\frac xr\right\rfloor\right).
\tag{12}
\]

Therefore

\[
\boxed{
A(x)-M(x)=
\sum_{\substack{1<r\le x\\r\in\mathcal R_Y}}
 (b_r-\mu(r))
 M_Y\!\left(\left\lfloor\frac xr\right\rfloor\right).
}
\tag{13}
\]

No asymptotic estimate enters this identity. It is the exact finite-scale defect left after exposing all prime directions through `Y`.

A first immediate recovery statement is

\[
\boxed{A(x)=M(x)\qquad(1\le x\le Y),}
\tag{14}
\]

because no nontrivial `Y`-rough core can occur below `Y`.

## 3. Polynomial breadth bounds the interaction order of the free core

Assume

\[
Y\ge H^\beta,
\qquad 0<\beta\le1.
\tag{15}
\]

If `r in R_Y`, `r<=H`, and `omega(r)=k`, then every prime divisor of `r` is strictly greater than `Y`, so

\[
r>Y^k\ge H^{\beta k}.
\tag{16}
\]

Thus `beta k>=1` would imply `r>H`, impossible. Hence `k<1/beta`, which is exactly (5):

\[
\omega(r)\le\left\lceil\frac1\beta\right\rceil-1.
\tag{17}
\]

This gives a deterministic hierarchy of residual interaction order. In particular,

\[
Y\ge\sqrt H
\quad\Longrightarrow\quad
\mathcal R_Y\cap[1,H]
=\{1\}\cup\{p:Y<p\le H,\ p\text{ prime}\}.
\tag{18}
\]

For a free prime `p>Y>=sqrt(H)` and `x<=H`,

\[
\left\lfloor\frac xp\right\rfloor
<\frac HY\le\sqrt H\le Y.
\tag{19}
\]

Consequently every integer contributing to the inner smooth sum is automatically `Y`-smooth, so `M_Y(floor(x/p))=M(floor(x/p))`. Equation (13) becomes the especially transparent identity

\[
\boxed{
A(x)=M(x)+
\sum_{Y<p\le x}(a_p+1)
M\!\left(\left\lfloor\frac xp\right\rfloor\right)
\qquad(Y\ge\sqrt H,\ x\le H).
}
\tag{20}
\]

Thus crossing the square-root breadth threshold destroys all genuinely higher-order rough-core sign freedom: the only deviations from Möbius are carried by individual primes beyond the enforced prefix. Equation (20) does not say those prime defects are harmless for GCD energy; it identifies exactly what remains to be controlled.

The exponent thresholds in (17) are one-way deterministic impossibility thresholds. They do not assert that all lower-order rough products actually occur with a useful density when `Y` falls below a threshold; such a density statement would require separate prime-distribution input.

## 4. Linear breadth collapses the GCD relaxation to one endpoint coordinate

Retain the Farey--Mertens horizon vector

\[
m_d^{(H)}:=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
m_{\mu,d}^{(H)}:=M\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\tag{21}
\]

and the square-GCD kernel

\[
K_H(d,e):=\frac{\gcd(d,e)^2}{de}.
\tag{22}
\]

If `Y>=H/2`, then for every `d>=2`,

\[
\left\lfloor\frac Hd\right\rfloor\le\frac H2\le Y,
\]

so (14) gives

\[
m_d^{(H)}=m_{\mu,d}^{(H)}\qquad(d\ge2).
\tag{23}
\]

For the endpoint, every free prime satisfies `p>Y>=H/2`, hence `floor(H/p)=1`. Equation (20) reduces to

\[
\boxed{
A(H)=M(H)+2k,
\qquad
0\le k\le \pi(H)-\pi(Y),
}
\tag{24}
\]

where `k` is exactly the number of free primes assigned sign `+1` instead of the Möbius sign `-1`. Every integer `k` in the displayed range is realizable by choosing that many primes.

Therefore the whole admissible GCD-horizon class is

\[
\boxed{
m^{(H)}=m_\mu^{(H)}+2k e_1,
\qquad
0\le k\le\pi(H)-\pi(Y).
}
\tag{25}
\]

In particular, the corresponding coordinate quotient is reduced exactly to the one-dimensional family

\[
R_H(k)=
\frac{(M(H)+2k)^2}
{(m_\mu^{(H)}+2ke_1)^T K_H(m_\mu^{(H)}+2ke_1)}.
\tag{26}
\]

This is an information reduction, not a new upper bound. `FD-003` shows that the unrestricted `H`-dimensional GCD problem has sharp limiting constant `zeta(2)`; (25)--(26) say that exposing a linear prime prefix removes every synthetic direction except one endpoint degree of freedom. Proving that (26) stays uniformly below the unrestricted equality value would require new information about the **physical Mertens tail** and is not supplied here.

## 5. Any unbounded exact prime prefix recovers a common source globally

Now let `a=(a_n)_(n>=1)` be one infinite source satisfying the global squarefree support/sign conditions in (1). Suppose there are sequences

\[
H_j\to\infty,
\qquad
Y_j\to\infty,
\qquad
1\le Y_j\le H_j,
\tag{27}
\]

such that for every `j`,

\[
a_{pn}=-a_n
\quad
(p\le Y_j\text{ prime},\ p\nmid n,\ pn\le H_j).
\tag{28}
\]

Fix a squarefree integer

\[
n=p_1p_2\cdots p_s.
\]

Choose `j` large enough that

\[
H_j\ge n,
\qquad
Y_j\ge\max_i p_i.
\tag{29}
\]

Starting from `a_1=1`, apply (28) successively along `p_1,...,p_s`. Every partial product is at most `n<=H_j`, so all steps are legal and

\[
a_n=(-1)^s=\mu(n).
\tag{30}
\]

Nonsquarefree coefficients are already zero. Since `n` was arbitrary, this proves (6).

The conclusion depends on **coverage**, not on the cardinality of the enforced set. `FD-028` may enforce infinitely many primes and remain non-Möbius because its prime set deliberately leaves infinitely many other prime directions free. An expanding initial segment is different: its union is the set of all primes, so on one common source every fixed squarefree coefficient is eventually determined.

The same argument works for any growing family of enforced prime sets whose eventual union contains every prime and whose horizon eventually contains each fixed finite product. The initial-segment formulation is the clean quantitative version relevant to the current breadth question.

## 6. Prior-art boundary and novelty discipline

The arithmetic ingredients are classical. The definition of `mu` already says that squarefree values are the parity of the number of prime factors, and multiplicativity makes the repeated sign flip in (8) immediate. Terence Tao, *A remark on partial sums involving the Möbius function*, Bull. Aust. Math. Soc. **81** (2010), 343--349, DOI `10.1017/S0004972709000884`, treats Möbius sums over multiplicative semigroups generated by arbitrary prime sets. Marco Aymone, *A note on multiplicative functions resembling the Möbius function*, J. Number Theory **212** (2020), 113--121, studies genuinely multiplicative squarefree-supported sign functions with small partial sums. These are neighboring boundaries already identified around `FD-027`--`FD-028`; neither is a load-bearing input here.

No novelty is claimed for splitting an integer into `Y`-smooth and `Y`-rough parts, for the identities defining the Möbius function, or for the observation that specifying all prime signs determines a multiplicative squarefree-supported function. The Mathia-specific content is the exact placement of that elementary fact inside the current Farey--Mertens control hierarchy: (13) classifies the residual finite-scale defect, (17) gives its deterministic interaction-depth profile, (20) identifies the square-root transition to prime-only defects, and (25) shows that linear breadth leaves only endpoint doping in the GCD horizon vector.

A literature search located the multiplicative-semigroup and Möbius-like-function work above but not a source needed to justify these exact finite identities. Because the proof is self-contained and those papers are contextual rather than load-bearing, `SOURCES.md` need not change for this finding.

## 7. Stress tests and falsification boundary

The result survives the main control ambiguities that matter here.

First, (4) is biconditional: it does not silently assume complete multiplicativity beyond the enforced small-prime directions. The rough-core signs remain independent variables at a fixed `(H,Y)`.

Second, the square-root claim uses strict roughness `p>Y`. When `Y=sqrt(H)`, two rough primes still have product strictly greater than `H`, so the prime-only conclusion remains valid at equality.

Third, (20) does not replace `M_Y` by `M` outside its valid range. The replacement occurs only after `Y>=sqrt(H)`, when every quotient `floor(x/p)` attached to a free prime is at most `Y`.

Fourth, the common-source conclusion requires the **same coefficient sequence** at every scale. Allowing a different synthetic sequence for every `H` removes the recovery argument; such scale-dependent controls remain legitimate finite-horizon relaxations and may still approach the unrestricted GCD constant.

Finally, none of (4)--(30) bounds `M(x)`, the Franel discrepancy, or the GCD quotient for the physical source. A falsification would require an admissible `(H,Y)` source not representable by (4), a rough core violating (17), a counterexample to the square-root decomposition (20), or a single non-Möbius common source satisfying (27)--(28).

## 8. Consequence for the live research question

`FD-027` and `FD-028` show that **finite breadth** and even **infinite sparse breadth** do not coerce sparse-horizon GCD non-saturation. The present result closes the opposite bookkeeping extreme: **exact complete prime-prefix breadth growing without bound on one common source eventually determines the source itself**.

The remaining useful target is therefore between those two regimes. A nontrivial source theorem should not merely say that more exact prime directions are exposed until all coefficients become Möbius. It should identify a quantitative condition whose information content is genuinely compressed relative to pointwise recovery and prove that this already damages the GCD equality-ray mechanism. The finite-scale rough-core decomposition (13) supplies a concrete language for that search: measure whether the surviving `Y`-rough defect mass, interaction order, or its projection onto the GCD equality ray can remain large as `Y=Y(H)` grows.

The first sharp structural checkpoint is now explicit:

\[
\boxed{
Y\ge\sqrt H
\quad\Longrightarrow\quad
\text{all residual source freedom up to }H\text{ is carried by individual primes }p>Y.
}
\tag{31}
\]

Whether that **prime-only residual class** can still asymptotically saturate the Farey--Mertens GCD dual bound at a single growing horizon is not answered here. That is a genuinely quantitative next problem; unlike simply letting the exact ancestry prefix tend to infinity on one fixed source, it does not collapse by pointwise reconstruction alone.
