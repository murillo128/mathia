# FD-141 — One infinite-precision additive coordinate can encode the full squarefree factorization

- **Date:** 2026-09-15
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** main-track boundary theorem / information-capacity result
- **Depends on:** FD-135, FD-139, FD-140

## Claim

The coordinate-incompleteness obstruction of FD-140 cannot be extended from fixed finite congruence alphabets to arbitrary fixed finite-dimensional strongly additive coordinates merely by counting coordinate dimension.

There exists a **single fixed real-valued strongly additive coordinate**

\[
F(n)=\sum_{p_j\mid n}3^{-j},
\]

where \(p_1<p_2<\cdots\) enumerates the primes, with the following properties.

1. \(F\) is injective on the squarefree integers. Hence the exact value of one scalar coordinate recovers the complete squarefree prime support.
2. Every statistic of the squarefree prime support — in particular every hidden prime-color coordinate or sign wall used in FD-138--FD-140 — is a function of the exact value of \(F\).
3. Conditioning an averaged prime-ancestry defect on an exact \(F\)-cell removes dilution completely: every nonempty squarefree cell contains one integer, so the conditional average is the pointwise edge defect.
4. This completeness is paid for entirely in precision. If

   \[
   \Delta_F(T):=
   \min_{\substack{m\ne n\le T\\ \mu^2(m)=\mu^2(n)=1}}
   |F(m)-F(n)|,
   \]

   then, for \(T\ge2\),

   \[
   \frac12\,3^{-\pi(T)}
   \le
   \Delta_F(T)
   \le
   3^{-\pi(T)}.
   \]

   Thus resolving all squarefree states up to \(T\) through this one-dimensional coordinate requires absolute precision on the scale \(3^{-\pi(T)}\), equivalently a worst-case precision budget of order \(\pi(T)\) bits.

Consequently, **coordinate dimension is not an information-capacity bound**. A meaningful completeness/no-go question after FD-140 must constrain the admissible information carried by the coordinates — for example through precision, entropy, regularity, source-native construction, or a controlled growing alphabet — rather than merely requiring a fixed finite number of additive coordinates.

The theorem is deliberately a boundary result. It does **not** claim that the coordinate \(F\) is source-native for Farey discrepancy, numerically stable, obtainable from the Franel/Fourier skeleton, or useful under finite precision. Its purpose is to rule out an over-broad diagonal argument.

## 1. Construction

Enumerate the primes increasingly,

\[
p_1=2<p_2=3<p_3=5<\cdots,
\]

and assign the superincreasing summable weights

\[
w_j:=3^{-j}.
\]

Define

\[
F(n):=\sum_{p_j\mid n}w_j
     =\sum_{p_j\mid n}3^{-j}.
\]

For every integer \(n\), this is a finite sum because \(n\) has finitely many prime divisors. It is strongly additive in the standard sense:

\[
F(p^k)=F(p)\qquad(k\ge1),
\]

and

\[
F(mn)=F(m)+F(n)
\qquad ((m,n)=1).
\]

The coordinate ignores prime powers, so it is not injective on all positive integers. That is irrelevant for the squarefree ancestry interfaces studied in FD-132--FD-140, where the state is the set of prime divisors.

The decisive property is strict tail dominance:

\[
w_j
=
3^{-j}
>
\sum_{k>j}3^{-k}
=
\frac12\,3^{-j}.
\]

This is stronger than ordinary uniqueness of a base expansion and gives a quantitative separation estimate.

## 2. Exact injectivity on the squarefree fiber

Let \(m\ne n\) be squarefree. Their prime-support sets differ. Let \(j_0\) be the smallest prime index belonging to exactly one of the two supports.

At index \(j_0\), the difference \(F(n)-F(m)\) contains a leading contribution of magnitude \(3^{-j_0}\). All contributions from larger indices have total absolute magnitude at most

\[
\sum_{j>j_0}3^{-j}
=
\frac12\,3^{-j_0}.
\]

Therefore

\[
|F(n)-F(m)|
\ge
3^{-j_0}-\frac12\,3^{-j_0}
=
\frac12\,3^{-j_0}
>0.
\]

Hence

\[
\boxed{
\mu^2(m)=\mu^2(n)=1,\quad F(m)=F(n)
\Longrightarrow
m=n.
}
\]

So the exact scalar value \(F(n)\) uniquely identifies the full prime support of every squarefree \(n\).

There is no base-expansion ambiguity hidden here. Each integer uses only finitely many digits, and the strict tail-dominance estimate above proves uniqueness directly; no convention about terminating versus repeating expansions is needed.

### General superincreasing version

The argument does not depend on the number \(3\). If \((w_j)_{j\ge1}\) is a positive summable sequence satisfying

\[
w_j>\sum_{k>j}w_k
\qquad\text{for every }j,
\]

then

\[
F_w(n):=\sum_{p_j\mid n}w_j
\]

is injective on squarefree integers by the same first-differing-index proof.

Thus the phenomenon is structural: one exact real coordinate can encode an arbitrarily large finite prime-support alphabet if arbitrarily fine digits are allowed.

## 3. Every hidden prime-color wall becomes visible

Let \(\mathcal S\) be any set of squarefree integers and let

\[
G:\mathcal S\to\mathbb C
\]

be any statistic whatsoever. Because \(F\) is injective on \(\mathcal S\), there is a function

\[
h:F(\mathcal S)\to\mathbb C
\]

defined by

\[
h(F(n)):=G(n)
\]

such that

\[
G(n)=h(F(n))
\qquad(n\in\mathcal S).
\]

No regularity of \(h\) is claimed or needed. This is exact measurability on the discrete image of the squarefree fiber.

In particular, take any real prime-coloring \(c(p)\) and its additive statistic

\[
D_c(n)=\sum_{p\mid n}c(p).
\]

On squarefree integers, \(D_c(n)\) is a function of \(F(n)\), because \(F(n)\) recovers the complete prime support. This includes the Dirichlet-character colorings used in FD-138--FD-140.

Therefore the FD-140 move

\[
\text{visible finite congruence alphabet}
\quad\leadsto\quad
\text{finer hidden prime color}
\]

cannot be iterated against this coordinate: there is no hidden prime-support statistic left once exact \(F\) is known.

This does not contradict FD-140. That theorem restricts the visible coordinates to a fixed finite congruence alphabet. The present \(F\) is deliberately nonperiodic in the prime index and has unbounded exact information content.

## 4. Exact-cell ancestry averages become pointwise

Fix a shell or other finite parent domain \(\mathcal S\), an active prime \(p\), and \(r>0\). For a value \(x\in F(\mathcal S)\), define the exact squarefree parent cell

\[
\mathcal C_{p,x}
:=
\{n\in\mathcal S:
  \mu^2(n)=1,
  p\nmid n,
  F(n)=x\}.
\]

Whenever \(\mathcal C_{p,x}\ne\varnothing\), injectivity gives

\[
|\mathcal C_{p,x}|=1.
\]

For any coefficient source \(a=(a_n)\), define the conditional ancestry defect

\[
\mathfrak E_{p,x,r}(a)
:=
\frac{1}{|\mathcal C_{p,x}|}
\sum_{n\in\mathcal C_{p,x}}
|a_{pn}+a_n|^r.
\]

If \(\mathcal C_{p,x}=\{n_x\}\), then identically

\[
\boxed{
\mathfrak E_{p,x,r}(a)
=
|a_{pn_x}+a_{n_x}|^r.
}
\]

Hence the thin-interface mechanism of FD-132, FD-134, FD-138, FD-139 and FD-140 has nowhere to dilute inside an exact \(F\)-cell. If one edge is wrong, its exact cell reports the full pointwise defect.

This is the same qualitative rigidity that made the \(L^\infty\) regime of FD-135 different from averaged ancestry, but obtained here by refining the conditioning sigma-algebra until every squarefree parent is isolated.

The statement is intentionally local. It does not by itself prove global recovery of Möbius, because one still has to specify which active primes and parent domains are controlled and how the resulting coefficient information connects to the Farey/Fourier target.

## 5. One scalar coordinate has maximal exact resolving cardinality

Define the resolving cardinality on the squarefree prefix by

\[
\mathcal N_F(T)
:=
\#\{F(n):n\le T,\ \mu^2(n)=1\}.
\]

Injectivity gives the exact identity

\[
\boxed{
\mathcal N_F(T)
=
\#\{n\le T:\mu^2(n)=1\}.
}
\]

No coordinate can distinguish more states than there are states. Thus, as an exact partition of the squarefree prefix, this **one-dimensional** coordinate has maximal possible resolving cardinality.

This is the simplest reason algebraic dimension cannot be used as a proxy for information capacity. The codomain is one-dimensional over \(\mathbb R\), but the number of exact distinguishable states grows with the entire squarefree prefix.

## 6. The precision tax is exponential in the prime alphabet

The previous sections would be misleading if the precision cost were left implicit. It is the essential obstruction to treating \(F\) as a practical or source-native coordinate.

Let

\[
\Delta_F(T)
:=
\min_{\substack{m\ne n\le T\\
                  \mu^2(m)=\mu^2(n)=1}}
|F(m)-F(n)|.
\]

Let \(J=\pi(T)\), so every prime divisor of an integer \(n\le T\) has index at most \(J\).

For distinct squarefree \(m,n\le T\), let \(j_0\le J\) be their first differing prime index. The argument from Section 2 gives

\[
|F(m)-F(n)|
\ge
\frac12\,3^{-j_0}
\ge
\frac12\,3^{-J}.
\]

Therefore

\[
\Delta_F(T)
\ge
\frac12\,3^{-\pi(T)}.
\]

For the opposite inequality, compare \(1\) with the largest prime \(p_J\le T\). Both are squarefree and

\[
|F(p_J)-F(1)|
=3^{-J}.
\]

Hence

\[
\Delta_F(T)
\le
3^{-\pi(T)}.
\]

Combining the two estimates,

\[
\boxed{
\frac12\,3^{-\pi(T)}
\le
\Delta_F(T)
\le
3^{-\pi(T)}.
}
\]

So exact recovery of every squarefree state up to \(T\) from a numerically represented value of \(F\) requires absolute resolution finer than a constant multiple of \(3^{-\pi(T)}\). In binary terms, the worst-case number of fractional bits needed to separate all states is

\[
\Theta(\pi(T)).
\]

The coordinate count stayed equal to one; the precision budget absorbed the growing prime alphabet.

This also supplies the matched control against overinterpreting the theorem. Under any fixed absolute quantization scale \(\delta>0\), choose distinct sufficiently large prime indices \(j<k\). Then

\[
|F(p_j)-F(p_k)|
=|3^{-j}-3^{-k}|
<\delta.
\]

Thus a fixed-precision observation cannot retain the exact injectivity at arbitrarily large scales. The completeness is genuinely an **infinite-precision** phenomenon.

## 7. Consequence for the research frontier

FD-139 showed that exact conditioning on the single central rank \(\omega(n)\) is incomplete: it fixes the total number of prime factors but leaves a transverse prime-color direction free. FD-140 enlarged the visible information to every count in a fixed finite congruence alphabet and showed that a finer prime coloring still escapes.

A tempting extrapolation would be:

> every fixed finite family of strongly additive prime-factor coordinates leaves another additive direction hidden.

That statement is false without an information restriction. The coordinate \(F\) above is a one-dimensional counterexample: it encodes the entire squarefree prime support exactly, so every other prime-support statistic is already measurable with respect to it.

The correct lesson is therefore not that a finite-dimensional coordinate system is necessarily incomplete. It is that the previous negative results concern coordinate systems with **bounded arithmetic resolution**. Once arbitrary exact real digits are allowed, dimension ceases to control resolution.

Accordingly, the next source-specific question should not be formulated solely in terms of the number of coordinates. Any useful notion of an admissible ancestry coordinate family must also control how much information those coordinates can carry. Natural possibilities include finite or quantified precision, bounded/growing alphabet complexity, regularity of the prime weights, an entropy or description-length budget, or a direct derivation from the Farey/Franel/Fourier observables.

The finding does not choose among those frameworks. It establishes why some such restriction is mathematically necessary before a general diagonal incompleteness theorem can be true.

## 8. Adversarial audit

### A. Is \(F\) really strongly additive?

Yes. Prime powers contribute once, and coprime products have disjoint prime supports. The construction is not completely additive over multiplicities, nor does it need to be.

### B. Is \(F\) injective on all integers?

No. It only sees the radical. The claim is restricted to squarefree integers, which is exactly the fiber on which the ancestry counterexamples FD-132--FD-140 were built.

### C. Can a base-expansion ambiguity destroy injectivity?

No. The proof uses strict tail dominance, not uniqueness conventions for infinite radix expansions. Every integer contributes a finite set of digits, and the first differing digit exceeds the entire possible tail.

### D. Is the coordinate secretly scale-dependent?

No. The prime enumeration and all weights \(3^{-j}\) are fixed once and for all. The same \(F\) works for every \(T\).

### E. Does one real number really count as one coordinate?

Algebraically yes, and that is precisely the boundary exposed here. Computationally or informationally it carries a growing number of significant digits. Section 6 quantifies that cost. The theorem shows why coordinate dimension alone is the wrong complexity measure.

### F. Does exact measurability imply stable decoding?

No. The decoding map on \(F(\mathcal S)\) can be arbitrarily irregular, and the minimum spacing shrinks like \(3^{-\pi(T)}\). No continuity, numerical stability, or finite-precision recovery is claimed.

### G. Does this prove a Farey discrepancy estimate or RH-equivalent bound?

No. It is an interface/boundary theorem about the coefficient-ancestry strategy. It rules out one over-broad no-go principle and identifies the missing resource accounting: information capacity.

### H. Does it contradict FD-140?

No. FD-140 concerns a fixed finite congruence-coordinate alphabet. The present coordinate is nonperiodic, assigns a distinct scale to every prime index, and has unbounded precision complexity. It lies exactly in the class that FD-140 left open.

## Conclusion

A fixed finite number of additive coordinates can be complete if exact real values are allowed to carry unbounded information. The explicit coordinate

\[
F(n)=\sum_{p_j\mid n}3^{-j}
\]

is one-dimensional, strongly additive, and injective on the squarefree fiber. It destroys every hidden prime-color wall under exact conditioning, but only by paying a minimum-spacing cost

\[
\Delta_F(T)=\Theta(3^{-\pi(T)}).
\]

Thus the post-FD-140 frontier is not **finite dimension versus another hidden direction**. It is **bounded information capacity versus enough arithmetic resolution to reconstruct the prime support**. Any future completeness or impossibility theorem for ancestry coordinates must account for that distinction.