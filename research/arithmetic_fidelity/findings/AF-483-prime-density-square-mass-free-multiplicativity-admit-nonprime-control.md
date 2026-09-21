# AF-483 — Prime density, square mass, and free multiplicativity admit a nonprime control

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INPUT`, `ARITHMETIC-FIDELITY`, `MATCHED-CONTROL`, `BEURLING-PRIMES`, `MULTIPLICATIVE-INDEPENDENCE`, `GIBBS-FIDELITY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-482 shows that the sharp global conditioning of the canonical prime Gibbs curve near `sigma=1` is already forced by the coarse counting law

\[
N_Q(x)\sim \frac{x}{\log x}
\]

together with the square-summable scalar

\[
P_Q(2)=\sum_{q\in Q}q^{-2}.
\]

A natural possible escape is that the rational primes also carry exact free multiplicative structure: their logarithms are linearly independent over `\mathbb Q`, equivalently distinct exponent vectors give distinct products. That extra structure still does not make the Gibbs data prime-specific.

Let

\[
\mathcal P=\{p_1<p_2<\cdots\}
\]

be the rational primes and let `epsilon_n>0` be arbitrary. There exists a strictly increasing sequence

\[
Q=\{q_1<q_2<\cdots\}\subset(1,\infty)
\]

such that:

1. every `q_n` is nonintegral and
   \[
   |q_n-p_n|<\epsilon_n;
   \tag{1}
   \]
2. the logarithms are linearly independent over `\mathbb Q`:
   \[
   \sum_n m_n\log q_n=0,
   \qquad m_n\in\mathbb Z
   \text{ finitely supported}
   \Longrightarrow m_n=0\ \forall n;
   \tag{2}
   \]
3. the exact square mass agrees with the rational-prime value:
   \[
   \boxed{
   \sum_n q_n^{-2}=\sum_p p^{-2}=P(2);
   }
   \tag{3}
   \]
4. the counting law is unchanged:
   \[
   \boxed{
   N_Q(x)\sim\frac{x}{\log x}.
   }
   \tag{4}
   \]

Thus `Q` is a Beurling-prime control whose generated numerical monoid has unique factorization in the chosen generators, just as the rational-prime monoid does, while none of its generators is an ordinary prime.

Applying AF-482 gives, for the canonical Gibbs family on `Q`,

\[
P_Q(\sigma_0)c_Q(\sigma_0)
\longrightarrow
\sqrt{\frac{P(2)}2}
\qquad(\sigma_0\downarrow1),
\tag{5}
\]

which is **exactly the same normalized sharp global boundary constant** as for the rational primes. Since `(4)` also gives

\[
P_Q(1+\varepsilon)\sim\log\frac1\varepsilon,
\]

the unnormalized margin has the same asymptotic

\[
\boxed{
 c_Q(1+\varepsilon)
 \sim
 \frac{\sqrt{P(2)/2}}{\log(1/\varepsilon)}
}
\tag{6}
\]

as the rational-prime Gibbs curve.

Therefore the package

\[
\boxed{
\text{prime-scale density}
+\text{ exact }P(2)
+\text{ one-crossing Gibbs geometry}
+\text{ free multiplicativity}
}
\]

still does **not** identify the rational primes. A prime-specific escape below AF-482 must retain structure stricter than unique numerical factorization or multiplicative independence, and stricter than the scalar square mass controlling the canonical Gibbs margin.

## Construction

The proof has two independent pieces. First build a multiplicatively independent tail by arbitrarily small one-sided perturbations of the primes. Then use two head coordinates to restore the exact square mass without destroying multiplicative independence.

### Step 1: a multiplicatively independent tail arbitrarily close to the primes

For `n>=3`, choose numbers `eta_n>0` so small that

\[
0<\eta_n<\min\{\epsilon_n,1,p_{n+1}-p_n\}
\tag{7}
\]

and so that any choice

\[
p_n<q_n<p_n+\eta_n
\tag{8}
\]

has total square-mass deficit as small as desired. For example, shrink `eta_n` until

\[
0<p_n^{-2}-(p_n+\eta_n)^{-2}<\delta 2^{-n}
\tag{9}
\]

for a small `delta>0` that will be fixed below.

Choose the `q_n`, `n>=3`, recursively. Suppose `q_3,\ldots,q_{n-1}` have already been chosen with logarithms linearly independent over `\mathbb Q`. A new value `q` creates an integer relation only if

\[
m\log q+\sum_{j=3}^{n-1}m_j\log q_j=0
\]

for some integers with `m\ne0`. Hence every forbidden value has the form

\[
q=\prod_{j=3}^{n-1}q_j^{-m_j/m}.
\tag{10}
\]

There are only countably many such values, while `(p_n,p_n+eta_n)` is an interval. Choose `q_n` outside the forbidden set. Induction gives

\[
\{\log q_n:n\ge3\}
\]

linearly independent over `\mathbb Q`.

Because `eta_n<1`, each `q_n` lies strictly between the integer `p_n` and `p_n+1`, so it is nonintegral. Also `(7)` preserves strict ordering.

Set

\[
D:=\sum_{n\ge3}\left(p_n^{-2}-q_n^{-2}\right)>0.
\tag{11}
\]

By `(9)`, `D` can be made arbitrarily small and the series converges absolutely.

### Step 2: restore `P(2)` with two head coordinates

Put

\[
A:=\frac14+\frac19+D.
\tag{12}
\]

For `t` just below `2`, define

\[
u(t):=\left(A-t^{-2}\right)^{-1/2}.
\tag{13}
\]

Then

\[
t^{-2}+u(t)^{-2}=A,
\tag{14}
\]

so choosing

\[
q_1=t,
\qquad
q_2=u(t)
\tag{15}
\]

forces

\[
q_1^{-2}+q_2^{-2}
+\sum_{n\ge3}q_n^{-2}
=
\frac14+\frac19+\sum_{n\ge3}p_n^{-2}.
\tag{16}
\]

This is exactly `(3)`.

When `D` is sufficiently small, there is a nonempty open interval `J` of values `t<2`, arbitrarily close to `2`, for which

\[
|t-2|<\epsilon_1,
\qquad
2<u(t)<3,
\qquad
|u(t)-3|<\epsilon_2.
\tag{17}
\]

Shrinking `J` if needed makes `q_1<q_2<q_3`; both head values are nonintegral.

It remains to choose `t` so that the two head coordinates do not introduce a multiplicative relation with the already fixed tail.

For every finitely supported integer vector `m=(m_1,m_2,m_3,\ldots)`, define

\[
F_m(t)
=
m_1\log t
+m_2\log u(t)
+\sum_{n\ge3}m_n\log q_n.
\tag{18}
\]

If `m_1=m_2=0`, tail independence already gives `F_m\ne0` for nonzero `m`. If `(m_1,m_2)\ne(0,0)`, then `F_m` is a real-analytic function on `J` and cannot vanish identically. Indeed,

\[
\frac{u'(t)}{u(t)}
=-\frac{t^{-3}}{A-t^{-2}},
\tag{19}
\]

so an identically vanishing derivative would imply

\[
\frac{m_1}{t}
-
\frac{m_2t^{-3}}{A-t^{-2}}
=0
\]

for every `t` in `J`, or equivalently

\[
m_1(At^2-1)-m_2=0
\tag{20}
\]

identically. Since `A>0`, `(20)` forces `m_1=m_2=0`, a contradiction.

Thus every nontrivial `F_m` has a discrete zero set. There are only countably many finitely supported integer vectors, so the union of all forbidden zero sets is countable. Choose

\[
t\in J
\]

outside that union. Then `(2)` holds for the full sequence `Q`.

This completes the construction.

## Counting law and Gibbs consequence

For `n>=3`, the construction gives

\[
p_n<q_n<p_n+1.
\tag{21}
\]

Hence, up to the harmless finite head modification,

\[
\pi(x-1)-O(1)
\le N_Q(x)
\le\pi(x)+O(1).
\tag{22}
\]

The prime number theorem therefore yields `(4)`.

The exact relation `(2)` has a separate consequence. If two generalized integers built from `Q` agree numerically,

\[
\prod_n q_n^{a_n}
=
\prod_n q_n^{b_n},
\]

then taking logarithms gives an integer relation, so `a_n=b_n` for every `n`. Thus the numerical Beurling integer system generated by `Q` is a free commutative monoid on the generators `q_n`; there are no accidental multiplicative collisions.

AF-478--AF-482 require no rational-prime identity for their Gibbs geometry. The likelihood ratio between two parameters is

\[
\frac{\mu^Q_\tau(q)}{\mu^Q_\sigma(q)}
=\frac{P_Q(\sigma)}{P_Q(\tau)}q^{-(\tau-\sigma)},
\]

which has one crossing for every strictly ordered positive generator sequence. Equation `(4)` supplies the boundary partition asymptotics, while `(3)` makes the AF-482 sharp global constant identical to the rational-prime constant. This proves `(5)` and `(6)`.

## What this rules out

AF-015 already shows that the bare free multiplicative monoid forgets the ordinary prime norm because arbitrary generator permutations remain automorphisms. AF-483 addresses a different possible escape: perhaps once a numerical norm has been retained, the additional fact that the generator norms are multiplicatively independent could restore rational-prime specificity.

It does not. The control `Q` simultaneously has:

- a numerical ordering and termwise norm values arbitrarily close to the ordinary primes;
- the same first-order prime counting law;
- exact equality of the global square mass `P_Q(2)=P(2)`;
- the same free numerical factorization property supplied by logarithmic `\mathbb Q`-independence;
- the same canonical Gibbs one-crossing mechanism;
- the same sharp local and global `1/log` Hilbert/TV boundary-conditioning asymptotic, including the leading constant.

So neither **unique factorization in the retained numerical generators** nor the AF-482 square-mass constant is the missing prime discriminator.

The result does not say that every multiplicative invariant is density-generic. It says that the most elementary exact multiplicative discriminator available after attaching numerical generator norms—absence of integer log relations—can be preserved by a nonprime control while the entire Gibbs package through AF-482 is also matched.

## Prior art and novelty audit

The ambient generalized-prime language and the role of logarithmic independence are classical or established.

- Arne Beurling, **“Analyse de la loi asymptotique de la distribution des nombres premiers généralisés. I,”** *Acta Mathematica* 68 (1937), 255–291, introduced generalized-prime systems and the corresponding generalized integers/zeta theory.
- Frederik Broucke, Athanasios Kouroupis, and Karl-Mikael Perfekt, **“A note on Bohr’s theorem for Beurling integer systems,”** *Mathematische Annalen* 389 (2024), 4319–4333, DOI `10.1007/s00208-023-02756-x`, explicitly work with increasing Beurling primes whose logarithms are linearly independent over `\mathbb Q`, so that the generated Beurling integers have unique product representations. They also develop small perturbations of Beurling prime systems.
- Frederik Broucke and Jasson Vindas, **“A new generalized prime random approximation procedure and some of its applications,”** *Mathematische Zeitschrift* 307 (2024), article 62, DOI `10.1007/s00209-024-03526-4`, gives strong discrete approximation procedures for constructing Beurling prime systems close to prescribed counting data. This makes perturbative matched generalized-prime controls established prior art rather than a Mathia novelty.
- The prime number theorem, used only to pass from the termwise bound `(21)` to `(4)`, is classical.

No novelty is claimed for Beurling primes, rational independence of logarithms, unique generalized-prime factorization under that independence, countable avoidance, or perturbative generalized-prime constructions. The exact two-coordinate compensation argument above is elementary.

The Arithmetic Fidelity contribution is the **matched-control synthesis** forced by the current frontier: after AF-482, one can additionally demand exact free multiplicativity and exact equality of the scalar `P(2)` controlling the sharp Gibbs margin, and a non-rational-prime system still survives all those gates simultaneously.

## Boundaries and falsification checks

- `Q` is a Beurling/generalized-prime control of positive real generator norms, not a second subset of the ordinary integers. Integrality, additive structure, congruence structure, or another property that intrinsically forces generator norms to be rational integers is not retained here and could distinguish the ordinary primes.
- Equality is imposed only for `P_Q(2)`, because that is the scalar entering the AF-482 leading constant. The construction does not claim equality of the full prime-zeta function. AF-017 already shows that exact Euler-product / prime-Dirichlet data in a convergence half-plane recover the generator-norm multiset, so matching all such data would force `Q=\mathcal P`.
- Termwise closeness and the counting law do not imply equality of finer gap, residue, additive-correlation, or higher Dirichlet data. Those are precisely candidate places where a genuine prime discriminator could live.
- Logarithmic `\mathbb Q`-independence is an exact free-factorization statement, not a quantitative Diophantine-separation bound. A downstream mechanism sensitive to quantitative near-relations would require a separate matched-control audit.
- The Gibbs conclusion uses AF-482 and therefore concerns the canonical normalized probability curve and its Hilbert/TV margin. It does not imply that every operator or spectral construction built from `Q` matches the rational-prime one.
- Nothing here has a direct RH consequence.

## Consequence for the line

AF-482 left a clear question: what structure lies strictly below density-class Gibbs geometry and can still certify rational-prime provenance? AF-483 removes one tempting answer. **Free multiplicativity is not enough, even when the generalized-prime control is arbitrarily close termwise to the ordinary primes and is tuned to reproduce the exact `P(2)` scalar that controls the sharp global Gibbs margin.**

The next useful discriminator must therefore use structure that this perturbative Beurling control cannot preserve automatically: additive/integral incidence, congruence or local-global arithmetic, exact higher Dirichlet data, quantitative log-relation geometry, or another intrinsically constrained relational layer. Any such candidate should be tested against controls that already satisfy `(1)`--`(4)` rather than against density-matched controls alone.